from django.contrib.postgres.search import SearchVector
from site_poslannik.models import Category, Parts

menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Контакты", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},

]


class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context: dict, **kwargs):
        context["menu"] = menu
        context["cats"] = Category.objects.all()
        context["title"] = "Автозапчасти в Борисове"
        context.update(kwargs)
        return context

    def get_mixin_queryset(self, **kwargs):
        if kwargs.get('cat_slug'):
            return Parts.objects.filter(category=Category.objects.get(slug=kwargs.get('cat_slug'))).order_by('name')[:1000]
        elif kwargs.get('query_string'):
            return Parts.objects.annotate(
                search=SearchVector('name', 'descr', 'category')).filter(search=kwargs.get('query_string'))
        else:
            return Parts.objects.all().order_by('name')[:1000]

