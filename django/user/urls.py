from django.urls import path
from .views import say_hello, get_user_list



urlpatterns = [
    path('', say_hello, name='users'),
]

urlpatterns = [
    path('', get_user_list, name='users')
]
