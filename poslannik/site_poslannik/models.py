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


# class SearchParts(models.Manager):
    # @staticmethod
    # def translit(str_ru, sep="-"):
    #     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
    #          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    #          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    #          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    #     res = ''
    #     for i in str_ru.lower():
    #         if i in t:
    #             res += t[i]
    #         elif i not in 'qwertyuiopasdfghjklzxcvbnm1234567890':
    #             res += sep
    #         else:
    #             res += i
    #
    #     while '--' in res:
    #         res = res.replace('--', '-')
    #
    #     return res

    # def get_queryset(self, q: str):
    #     q = self.translit(q)
    #     req_words = q.split('-')
    #     queryes = ''
    #     for word in req_words:
    #         temp = super().get_queryset().filter(Q(slug__icontains=word))
    #         if not temp:
    #
    #             temp = None
    #
    #             for i in range(len(word)):
    #
    #                 temp_w = super().get_queryset().filter(Q(name__icontains=word[:i]))
    #
    #                 if temp_w:
    #                     temp = word[:i]
    #                 else:
    #                     break
    #
    #             queryes += temp + '-'
    #         else:
    #             queryes += word + '-'
    #
    #     queryes = queryes.strip('-')
    #     return super().get_queryset().filter(slug__icontains=queryes)



# Create your models here.
class Parts(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(unique=True, primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    descr = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True, default='', db_index=True)

    # objects = models.Manager()
    # search = SearchParts

    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})
