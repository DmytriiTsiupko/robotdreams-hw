from .models import Purchase
from .forms import PurchaseForm

from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from .serializers import PurchaseSerializer


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseListView(ListView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase-list')


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


