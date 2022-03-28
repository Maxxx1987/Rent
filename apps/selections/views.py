from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView

from apps.selections.forms import SelectionForm
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


class SelectionDetailView(DetailView):
    model = Selection
