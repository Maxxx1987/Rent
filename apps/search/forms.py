from django import forms


class SearchForm(forms.Form):
    term = forms.CharField(min_length=3)
