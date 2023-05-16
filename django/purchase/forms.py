from django import forms
from .models import Purchase, Book


class PurchaseForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all(),
                                           widget=forms.SelectMultiple(attrs={'class': 'form-select'}))

    class Meta:
        model = Purchase
        fields = ('id', 'quantity', 'total_price')
