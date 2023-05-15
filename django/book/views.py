from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Book


class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book

