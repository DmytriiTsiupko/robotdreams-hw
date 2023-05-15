from .models import Purchase
from django.views.generic import ListView, DetailView


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseListView(ListView):
    model = Purchase
