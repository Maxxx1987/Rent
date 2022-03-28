from django.db import models
from autoslug import AutoSlugField


class Product(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='mediafiles/covers/%Y/%m/%d', blank=True)
    section = models.ForeignKey('catalog.Section', on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField('Цена', default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/{self.id}/'


class ProductInfo(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product_info')
    name = models.CharField('Название', max_length=255)
    value = models.CharField('Значение', max_length=255, default='N/A')

    class Meta:
        verbose_name = 'Характеристика'

    def __str__(self):
        return f'{self.name}: {self.value}'
