from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def get_all_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)
