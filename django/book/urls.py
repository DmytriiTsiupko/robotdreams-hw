from django.urls import path
from .views import get_all_books


urlpatterns = [
    path('', get_all_books, name='books')
]
