from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView

from apps.selections.forms import SelectionForm, ProductSelectionForm
from apps.selections.models import ProductSelection, Selection


class SelectionListView(ListView):
    model = Selection


class SelectionCreateView(CreateView):
    model = Selection
    form_class = SelectionForm
    success_url = '/selections/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SelectionDeleteView(DeleteView):
    model = Selection
    success_url = '/selections/'


class ProductSelectionListView(ListView):
    model = ProductSelection
    template_name = 'selections/selection_detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(selection=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['selection'] = Selection.objects.get(id=self.kwargs['pk'])
        context['form'] = ProductSelectionForm(initial={'selection': self.kwargs['pk']})
        return context


class ProductSelectionCreateView(CreateView):
    model = ProductSelection
    form_class = ProductSelectionForm

    def get_success_url(self):
        return self.object.selection.get_absolute_url()


class ProductSelectionDeleteView(DeleteView):
    model = ProductSelection

    def get_success_url(self):
        return self.object.selection.get_absolute_url()
