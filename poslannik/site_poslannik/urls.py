from django.urls import path, include
from . import views
from .converters import *
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('part/<slug:part_slug>/', views.show_part, name='part'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('archive/<yyyy:year>/', views.archive, name='arhive'),
    path('category/<slug:cat_slug>/', views.cats, name='category'),
    path('searchpart/', views.search, name='search'),
]