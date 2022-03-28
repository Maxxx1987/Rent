from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.payments.form import ProductOrderForm, ProductOrderUpdateForm
from apps.payments.models import ProductOrder, Order


class ProductOrderCreateView(CreateView):
    model = ProductOrder
    form_class = ProductOrderForm

    def get_success_url(self):
        return self.object.product.get_absolute_url()

    def form_valid(self, form):
        user_active_order, created = Order.objects.get_or_create(user=self.request.user, status='active')
        form.instance.order = user_active_order
        return super().form_valid(form)


class ProductOrderListView(ListView):
    model = ProductOrder
    context_object_name = 'productorder_list'
    template_name = 'products/productorder_list.html'

    def get(self, request, *args, **kwargs):
        self.order = Order.objects.get(user=self.request.user, status='active')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(order=self.order)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['identifier'] = self.order.identifier

        order_sum = 0
        for item in context['productorder_list']:
            item.form = ProductOrderUpdateForm(instance=item)
            order_sum += item.count * item.product.price

        context['order_sum'] = order_sum
        return context


class ProductOrderUpdateView(UpdateView):
    model = ProductOrder
    form_class = ProductOrderUpdateForm
    success_url = '/order/list/'


class ProductOrderDeleteView(DeleteView):
    model = ProductOrder
    success_url = '/order/list/'
