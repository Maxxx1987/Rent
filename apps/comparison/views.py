from django.views.generic import ListView, DeleteView, CreateView

from apps.comparison.forms import ComparisonProductForm
from apps.comparison.models import Comparison, ComparisonProduct


class ComparisonProductListView(ListView):
    model = ComparisonProduct
    context_object_name = 'comparison_list'
    template_name = 'comparison/comparison_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(comparison__user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['comp'] = Comparison.objects.filter(user=self.request.user).first()
        return context


class ComparisonProductDeleteView(DeleteView):
    model = ComparisonProduct
    success_url = '/comparison/list/'


class ComparisonDeleteView(DeleteView):
    model = Comparison
    success_url = '/comparison/list/'


class ComparisonProductCreateView(CreateView):
    model = ComparisonProduct
    form_class = ComparisonProductForm

    def form_valid(self, form):
        comparison, created = Comparison.objects.get_or_create(user=self.request.user)
        form.instance.comparison = comparison
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.product.get_absolute_url()
