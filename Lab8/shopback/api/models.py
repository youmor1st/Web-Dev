from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="name of category")

    def ___str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name of product")
    price = models.CharField(max_length=100, null=False, blank=False, verbose_name="price of product")
    description = models.TextField(null=True, blank=True, verbose_name="description of product")
    count = models.IntegerField(null=False, blank=False, verbose_name="amount of Product")
    is_active = models.BooleanField(null=False, blank=False, verbose_name='is_active status')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name} - Price: {self.price}'
