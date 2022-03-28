from django.contrib import admin
from apps.selections.models import Selection


@admin.register(Selection)
class ProductAdmin(admin.ModelAdmin):
    pass
