from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},

]

data_db = [
    {"id": 1, 'title': 'ГАЗ', 'content': 'Двигатели', 'is_published': True},
    {"id": 2, 'title': 'УАЗ', 'content': 'Колеса', 'is_published': True},
    {"id": 3, 'title': 'ВАЗ', 'content': 'Коленвалы', 'is_published': True},
]

cats_db = [
    {"id": 3, 'title': "Запчасти на ВАЗ"},
    {"id": 2, 'title': "Запчасти на УАЗ"},
    {"id": 1, 'title': "Запчасти на ГАЗ"},

]


def index(request):
    data = {
        'title': 'Автозапчасти в Борисове',
        'menu': menu,
        'parts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'site_poslannik/index.html', context=data)


def login(request):
    return HttpResponse('<h1>Login</h1>')


def contact(request):
    return HttpResponse('<h1>Контакты: 80-177-76-36-02</h1>')


def show_part(request, part_id):
    return HttpResponse(f'Запчасть {part_id}')


def about(request):
    return render(request, 'site_poslannik/about.html', {'title': 'О нас', 'menu': menu})


def cats(request, cat_id):
    data = {
        'parts': data_db,
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'site_poslannik/category.html', context=data)


def archive(request, year):
    if year > 2023:
        uri = reverse('cats_slug', args=('bebracat2000',))
        return redirect(uri)
    return HttpResponse(f'In {year} year... ')


def page_not_found(request, exception):
    return redirect(index)
