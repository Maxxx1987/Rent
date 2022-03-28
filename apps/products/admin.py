from django.contrib import admin

from apps.products.models import Product, ProductInfo


class ProductInLine(admin.TabularInline):
    model = ProductInfo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [ProductInLine]


