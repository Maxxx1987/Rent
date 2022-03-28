from django.db import models


class Selection(models.Model):
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    price = models.PositiveIntegerField('Цена', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
        ordering = ('-id',)

    def get_absolute_url(self):
        return f'/selections/{self.id}/'


class ProductSelection(models.Model):
    selection = models.ForeignKey('selections.Selection', on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
