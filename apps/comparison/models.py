from django.db import models


class Comparison(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ComparisonProduct(models.Model):
    comparison = models.ForeignKey('comparison.Comparison', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
