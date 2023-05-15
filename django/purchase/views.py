from .models import Purchase
from .forms import PurchaseForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseListView(ListView):
    model = Purchase


class PurchaseFormView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase-list')

