from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    text = models.TextField('текст отзыва', blank=True, null=True)
    rating = models.PositiveIntegerField('Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created_at',)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return f'/reviews/{self.id}/'
