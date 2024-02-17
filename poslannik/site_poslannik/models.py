from django.db import models


# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True, primary_key=True)
    descr = models.TextField(blank=True)
