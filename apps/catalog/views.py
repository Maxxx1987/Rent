from django.views.generic import ListView, TemplateView

from apps.catalog.models import Category, Section


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryListView(ListView):
    queryset = Category.objects.filter(is_active=True)
    context_object_name = 'category_list'


class SectionListView(ListView):
    queryset = Section.objects.filter(is_active=True)
    context_object_name = 'section_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(category__slug=self.kwargs['slug'])
