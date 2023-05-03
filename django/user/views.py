from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User


def say_hello(request):
    return HttpResponse('Hello, users!')


def get_user_list(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

