from django.views.generic import ListView, DetailView
from django.db.models import Avg, Q

from apps.comparison.forms import ComparisonProductForm
from apps.comparison.models import ComparisonProduct
from apps.products.models import Product, ProductInfo
from apps.payments.form import ProductOrderForm
from apps.payments.models import ProductOrder
from apps.reviews.models import Review


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(section__slug=self.kwargs['bar'])


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product_info'] = ProductInfo.objects.filter(product__pk=self.kwargs['pk'])

        p_order = (
            ProductOrder.objects
            .filter(product=self.object, order__user=self.request.user)
            .first()
        )
        if not p_order:
            context['order_form'] = ProductOrderForm(initial={'product': self.object.id})

        context['review_list'] = (
            Review.objects
            .filter(product=self.object)
            .exclude(Q(text__isnull=True) | Q(text='') | Q(user=self.request.user))
        )
        agg_rating = (
            Review.objects
            .filter(product=self.object)
            .aggregate(rating=Avg('rating'))
        )
        context['product_avg_rating'] = round(agg_rating['rating'], 1) if agg_rating['rating'] else '-'
        context['my_review'] = Review.objects.filter(product=self.object, user=self.request.user).first()

        p_comparison = (
            ComparisonProduct.objects
            .filter(product=self.object, comparison__user=self.request.user)
            .first()
        )
        if not p_comparison:
            context['comparison_form'] = ComparisonProductForm(initial={'product': self.object.id})

        return context
