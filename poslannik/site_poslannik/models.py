from django.db import models


# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True, primary_key=True)
    category = models.IntegerField(verbose_name='cat', default=1)
    descr = models.TextField(blank=True)
