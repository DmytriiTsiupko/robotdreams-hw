from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book-list')




