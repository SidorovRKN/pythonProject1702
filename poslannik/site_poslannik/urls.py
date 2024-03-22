from django.urls import path, include
from . import views
from .converters import *
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('part/<slug:part_slug>/', views.ShowPartView.as_view(), name='part'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('archive/<yyyy:year>/', views.ArchiveView.as_view(), name='archive'),  # Использование int вместо yyyy
    path('category/<slug:cat_slug>/', views.IndexView.as_view(), name='category'),
    path('searchpart/', views.SearchView.as_view(), name='search'),
    path('addpart/', views.AddPartView.as_view(), name='addpart')
]