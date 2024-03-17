from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, db_index=True)
    descr = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True)
    public = models.BooleanField(verbose_name='Опубликовано', default=True)
    # objects = models.Manager()
    # search = SearchParts

    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})
