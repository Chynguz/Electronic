from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название: ')
    description = models.TextField(verbose_name='Описание: ')
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
