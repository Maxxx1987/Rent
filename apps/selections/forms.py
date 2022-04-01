from django import forms

from apps.selections.models import ProductSelection, Selection


class SelectionForm(forms.ModelForm):

    class Meta:
        model = Selection
        fields = ['name', ]


class ProductSelectionForm(forms.ModelForm):

    class Meta:
        model = ProductSelection
        fields = ['selection', 'product']
        widgets = {
            'selection': forms.HiddenInput()
        }
