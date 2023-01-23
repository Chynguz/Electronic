from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название: ')
    description = models.TextField(verbose_name='Описание: ')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
