from django.views.generic import FormView

from apps.search.forms import SearchForm
from apps.products.models import Product


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        title = form.cleaned_data['term']
        products = Product.objects.filter(title__icontains=title)
        return self.render_to_response(self.get_context_data(product_list=products))
