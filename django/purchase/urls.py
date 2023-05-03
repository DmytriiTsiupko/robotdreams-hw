from django.urls import path
from .views import get_all_purchases

urlpatterns = [
    path('', get_all_purchases, name='purchases')
]