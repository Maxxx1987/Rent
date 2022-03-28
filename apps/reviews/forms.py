from django import forms

from apps.reviews.models import Review


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text', 'product', 'rating']
        widgets = {
            'product': forms.HiddenInput()
        }
