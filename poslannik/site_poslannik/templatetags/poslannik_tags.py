from django import template
import site_poslannik.views as views
from site_poslannik.models import Category

register = template.Library()




@register.inclusion_tag('site_poslannik/autocats.html')
def show_categories(cat_slug):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_slug': cat_slug}
