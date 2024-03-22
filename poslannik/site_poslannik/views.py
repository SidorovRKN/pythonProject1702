from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views import View
from django.views.generic import ListView, DetailView
from site_poslannik.models import Parts, Category

# Create your views here.
menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},

]


class IndexView(ListView):
    template_name = 'site_poslannik/index.html'
    context_object_name = 'parts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["cats"] = Category.objects.all()
        context["title"] = "Автозапчасти в Борисове"

        # костыль пока нет описаний
        context["default_descr"] = "Описание товара № ХХХХ"

        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            context["cat_selected"] = cat_slug
        part_slug = self.kwargs.get('part_slug')
        if part_slug:
            context["part"] = Parts.objects.get(slug=part_slug)
        return context

    def get_queryset(self):
        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            cat_selected = Category.objects.get(slug=cat_slug)
            return Parts.objects.filter(category=cat_selected).order_by('name')[:20]
        else:
            return Parts.objects.all().order_by('name')[:20]



class ShowPartView(DetailView):
    model = Parts
    template_name = 'site_poslannik/part.html'
    context_object_name = 'part'
    slug_field = 'slug'  # Поле в модели, используемое как slug
    slug_url_kwarg = 'part_slug'  # Имя параметра в URLconf, которое содержит slug

class AddPartView(View):
    def get(self, request):
        data = {
            'title': f'Добавить запчасть',
            'menu': menu,
            'cats': Category.objects.all(),
        }
        return render(request, 'site_poslannik/addpart.html', context=data)


class AboutView(View):
    def get(self, request):
        return render(request, 'site_poslannik/about.html', {'title': 'О нас', 'menu': menu})


class SearchView(View):
    def get(self, request):
        query_string = request.GET.get('q')
        parts = Parts.objects.annotate(search=SearchVector('name', 'descr', 'category')).filter(search=query_string)
        data = {
            'title': 'Автозапчасти в Борисове',
            'menu': menu,
            'parts': parts,
            'cats': Category.objects.all()
        }
        return render(request, 'site_poslannik/search.html', data)


class ArchiveView(View):
    def get(self, request, year):
        if year > 2023:
            uri = reverse('cats_slug', args=('bebracat2000',))
            return redirect(uri)
        return HttpResponse(f'In {year} year... ')


class LoginView(View):
    def get(self, request):
        return HttpResponse('<h1>Login</h1>')


class ContactView(View):
    def get(self, request):
        data = {
            'title': 'Контакты для заказа',
            'num': '76-36-02',
            'menu': menu,
            'email': 'some_email@gmail.com',
            'cats': Category.objects.all()
        }
        return render(request, 'site_poslannik/contact.html', context=data)


def page_not_found(request, exception):
    return redirect(IndexView.as_view)
