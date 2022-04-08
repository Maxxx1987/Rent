from django.contrib import admin
from apps.comparison.models import Comparison


@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    pass
