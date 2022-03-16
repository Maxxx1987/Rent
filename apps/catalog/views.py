from django.views.generic import ListView, TemplateView

from apps.catalog.models import Category, Section


class MenuMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = Category.objects.all()
        return context


class IndexView(MenuMixin, TemplateView):
    template_name = 'index.html'


class CategoryListView(MenuMixin, ListView):
    queryset = Category.objects.filter(is_active=True)
    context_object_name = 'category_list'


class SectionListView(MenuMixin, ListView):
    queryset = Section.objects.filter(is_active=True)
    context_object_name = 'section_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(category__slug=self.kwargs['slug'])
