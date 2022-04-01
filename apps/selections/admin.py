from django.contrib import admin
from apps.selections.models import Selection, ProductSelection


@admin.register(Selection)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductSelection)
class ProductSelectionAdmin(admin.ModelAdmin):
    pass
