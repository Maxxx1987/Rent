from django.db import models


class Payment(models.Model):
    STATUSES = (
        ('new', 'Новый'),
        ('pending', 'Обрабатывается'),
        ('error', 'Ошибка'),
        ('success', 'Успешно'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    status = models.CharField('Статус', max_length=16, choices=STATUSES, default='new')
    amount = models.IntegerField('Цена', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-id',)


class Purchase(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    payment = models.ForeignKey('payments.Payment', on_delete=models.PROTECT)
    rent_from = models.DateTimeField()
    rent_till = models.DateTimeField()

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('-id',)
