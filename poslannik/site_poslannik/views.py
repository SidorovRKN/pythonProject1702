from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from site_poslannik.models import Parts, Category

# Create your views here.
menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},

]


def index(request):
    data = {
        'title': 'Автозапчасти в Борисове',
        'menu': menu,
        'parts': Parts.objects.all()[:20],
        'cats': Category.objects.all()
    }
    return render(request, 'site_poslannik/index.html', context=data)


def show_part(request, part_slug):
    part = get_object_or_404(Parts, slug=part_slug)

    data = {
        'title': f'{part.name}',
        'name': part.name,
        'menu': menu,
        'part': part,
        'cats': Category.objects.all()
    }

    return render(request, 'site_poslannik/part.html', context=data)


def about(request):
    return render(request, 'site_poslannik/about.html', {'title': 'О нас', 'menu': menu})


def cats(request, cat_slug):
    selected = Category.objects.get(slug=cat_slug)
    data = {
        'title': f'{selected.name}',
        'parts': selected.parts_set.all()[:20],
        'menu': menu,
        'cat_selected': cat_slug,
        'cats': Category.objects.all()
    }
    return render(request, 'site_poslannik/index.html', context=data)


def search(request):
    query_string = request.GET.get('q')
    parts = Parts.objects.annotate(search=SearchVector('name', 'descr', 'category')).filter(search=query_string)
    data = {
        'title': 'Автозапчасти в Борисове',
        'menu': menu,
        'parts': parts,
        'cats': Category.objects.all()
    }
    return render(request, 'site_poslannik/search.html', data)


def archive(request, year):
    if year > 2023:
        uri = reverse('cats_slug', args=('bebracat2000',))
        return redirect(uri)
    return HttpResponse(f'In {year} year... ')


def login(request):
    return HttpResponse('<h1>Login</h1>')


def contact(request):
    data = {
        'title': 'Контакты для заказа',
        'num': '76-36-02',
        'menu': menu,
        'email': 'some_email@gmail.com',
        'cats': Category.objects.all()

    }
    return render(request, 'site_poslannik/contact.html', context=data)


def page_not_found(request, exception):
    return redirect(index)
