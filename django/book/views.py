from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm
from .filters import BookFilter
from .serializers import BookSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


# ==== VIEWS ====

class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book-list')


# ==== VIEW SETS ====

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'price']



