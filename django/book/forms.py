from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def get_success_url(self):
        return revers('book-detail', rgs=[self.id])
