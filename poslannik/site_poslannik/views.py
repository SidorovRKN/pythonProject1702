from django.db.models import Q
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


def translit(str_ru, sep="-"):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for i in str_ru.lower():
        if i in t:
            res += t[i]
        elif i not in 'qwertyuiopasdfghjklzxcvbnm1234567890':
            res += sep
        else:
            res += i

    while '--' in res:
        res = res.replace('--', '-')

    return res


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
    q = translit(request.GET.get('q'))
    req_words = q.split('-')
    query = ''
    for word in req_words:
        temp = Parts.objects.filter(Q(slug__icontains=query + word))
        if not temp:

            temp = None

            for i in range(len(word)):

                temp_w = Parts.objects.filter(Q(slug__icontains=query + word[:i]))
                print(temp_w)
                print(word[:i])
                if temp_w:
                    temp = word[:i]
                else:
                    break

            query += temp + '-'
        else:
            query += word + '-'

    query = query.strip('-')
    print(query)
    data = {
        'title': 'Автозапчасти в Борисове',
        'menu': menu,
        'parts': Parts.objects.filter(slug__icontains=query),
        'cats': Category.objects.all()
    }
    return render(request, 'site_poslannik/index.html', context=data)


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
