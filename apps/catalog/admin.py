from django.contrib import admin

from apps.catalog.models import Category, Section


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)

