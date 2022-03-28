from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.reviews.forms import AddReviewForm
from apps.reviews.models import Review


class ReviewViewMixin:

    def get_success_url(self):
        return self.object.product.get_absolute_url()


class ReviewListView(ListView):
    model = Review
    template_name = 'product_detail.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(product__pk=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['product_slug'] = self.kwargs['slug']
        return context


class ReviewCreateView(ReviewViewMixin, CreateView):
    model = Review
    form_class = AddReviewForm

    def get_initial(self):
        initial = super().get_initial()
        initial['product'] = self.kwargs['pk']
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(ReviewViewMixin, UpdateView):
    model = Review
    form_class = AddReviewForm


class ReviewDeleteView(ReviewViewMixin, DeleteView):
    model = Review
