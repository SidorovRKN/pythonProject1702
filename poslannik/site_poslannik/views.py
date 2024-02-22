from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string

from site_poslannik.models import Parts, Category


# Create your views here.
menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},

]


cats_db = [
    {"id": 1, 'title': "Запчасти на ГАЗ"},
    {"id": 2, 'title': "Запчасти на УАЗ"},
    {"id": 3, 'title': "Запчасти на ВАЗ"},

]


PARTS = Parts.objects.all()

def index(request):
    data = {
        'title': 'Автозапчасти в Борисове',
        'menu': menu,
        'parts': PARTS[:20],
        'cat_selected': 0,
    }
    return render(request, 'site_poslannik/index.html', context=data)


def login(request):
    return HttpResponse('<h1>Login</h1>')


def contact(request):
    data = {
        'title': 'Контакты для заказа',
        'num': '76-36-02',
        'menu': menu,
        'email': 'some_email@gmail.com',
    }
    return render(request, 'site_poslannik/contact.html', context=data)


def show_part(request, part_slug):
    part = get_object_or_404(Parts, slug=part_slug)

    data = {
        'title': f'{part.name}',
        'name': part.name,
        'menu': menu,
        'part': part,
        'cat_selected': 1,
    }

    return render(request, 'site_poslannik/part.html', context=data)


def about(request):
    return render(request, 'site_poslannik/about.html', {'title': 'О нас', 'menu': menu})


def cats(request, cat_slug):
    selected = Category.objects.filter(slug=cat_slug)[0]
    # parts = Parts.objects.filter(category=selected)[:20]
    data = {
        'title': f'{selected.name}',
        'parts': selected.parts_set.all(),
        'menu': menu,
        'cat_selected': cat_slug,
    }
    return render(request, 'site_poslannik/category.html', context=data)


def archive(request, year):
    if year > 2023:
        uri = reverse('cats_slug', args=('bebracat2000',))
        return redirect(uri)
    return HttpResponse(f'In {year} year... ')


def page_not_found(request, exception):
    return redirect(index)
