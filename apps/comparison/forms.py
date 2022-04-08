from django import forms
from apps.comparison.models import Comparison, ComparisonProduct


class ComparisonProductForm(forms.ModelForm):

    class Meta:
        model = ComparisonProduct
        fields = ['product',]
        widgets = {
            'product': forms.HiddenInput(),
        }
