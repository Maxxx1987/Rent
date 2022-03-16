from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    slug = AutoSlugField(populate_from='title')
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order', 'slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/catalog/{self.slug}/'


class Section(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, related_name='sections')
    slug = AutoSlugField(populate_from='title')
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('order', 'slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/catalog/{self.category.slug}/{self.slug}/'
