from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

class Category(models.Model):
    name = models.CharField(verbose_name='Наименование',max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Create your models here.
class Parts(models.Model):
    name = models.CharField(verbose_name='Наименование',max_length=200, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, db_index=True,verbose_name='Категория')
    descr = models.TextField(verbose_name='Описание',blank=True, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, db_index=True)
    public = models.BooleanField(verbose_name='Опубликовано', default=True)
    # objects = models.Manager()
    # search = SearchParts

    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"