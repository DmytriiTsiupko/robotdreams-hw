from django.shortcuts import render
from .models import Purchase
from django.http import JsonResponse


def get_all_purchases(request):
    purchases = list(Purchase.objects.values())
    return JsonResponse(purchases, safe=False)
