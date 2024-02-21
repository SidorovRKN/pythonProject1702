from django.db import models


# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True, primary_key=True)
    category = models.IntegerField(verbose_name='cat', default=1)
    descr = models.TextField(blank=True)
    slug = models.SlugField(max_length=255,blank=True, default='')




# class PartsAuto(models.Model):
#     index = models.BigIntegerField(primary_key=True)
#     sclad = models.TextField(db_column='SCLAD', blank=True, null=True)  # Field name made lowercase.
#     grup = models.TextField(db_column='GRUP', blank=True, null=True)  # Field name made lowercase.
#     nnum = models.TextField(db_column='NNUM', blank=True, null=True)  # Field name made lowercase.
#     name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
#     crc = models.BigIntegerField(db_column='CRC', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'parts_auto'
#
#     def __str__(self):
#         return f'{self.name}'