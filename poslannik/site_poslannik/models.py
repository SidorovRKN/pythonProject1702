from django.db import models
from django.urls import reverse
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True, primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    descr = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True, default='', db_index=True)

    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})


