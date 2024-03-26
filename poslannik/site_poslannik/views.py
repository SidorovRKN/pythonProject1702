from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from site_poslannik.models import Parts, Category

from site_poslannik.utils import DataMixin


# Create your views here.

class IndexView(DataMixin, ListView):
    template_name = 'site_poslannik/index.html'
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_slug = self.kwargs.get('cat_slug')
        return self.get_mixin_context(context, default_descr="Описание товара № ХХХХ", cat_selected=cat_slug)

    def get_queryset(self):
        cat_slug = self.kwargs.get('cat_slug');
        query_string = self.request.GET.get('q')
        parts = self.get_mixin_queryset(cat_slug=cat_slug, query_string=query_string)
        paginator = Paginator(parts, 20)
        page_number = self.request.GET.get('page')
        print(page_number)
        page = paginator.get_page(page_number)
        print(page)
        return page

class ShowPartView(DataMixin, DetailView):
    model = Parts
    template_name = 'site_poslannik/part.html'
    context_object_name = 'part'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        part_slug = self.kwargs.get('slug')
        part = Parts.objects.get(slug=part_slug)
        return self.get_mixin_context(context, title=part.name, part=part, default_descr=f"Описание товара № {part.pk}")


# class AddPartView(View):
#     def get(self, request):
#         data = {
#             'title': f'Добавить запчасть',
#             'menu': menu,
#             'cats': Category.objects.all(),
#         }
#         return render(request, 'site_poslannik/addpart.html', context=data)


class AboutView(DataMixin, TemplateView):
    template_name = "site_poslannik/about.html"
    title_page = 'О нас'
    extra_context = {
        'cats': Category.objects.all()
    }


# class ArchiveView(View):
#     def get(self, request, year):
#         if year > 2023:
#             uri = reverse('cats_slug', args=('bebracat2000',))
#             return redirect(uri)
#         return HttpResponse(f'In {year} year... ')


class LoginView(View):
    def get(self, request):
        return HttpResponse('<h1>Login</h1>')


class ContactView(DataMixin, TemplateView):
    template_name = "site_poslannik/contact.html"
    title_page = 'Контакты'

    extra_context = {
        'title': 'Контакты для заказа',
        'num': '76-36-02',
        'email': 'some_email@gmail.com',
        'cats': Category.objects.all()
    }


def page_not_found(request, exception):
    return redirect(IndexView.as_view)


def servererror(request):
    return redirect('home')
