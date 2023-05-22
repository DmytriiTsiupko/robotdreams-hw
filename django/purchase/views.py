from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Purchase
from .forms import PurchaseForm
from .serializers import PurchaseSerializer
from .filters import PurchaseFilter

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters



# ==== VIEWS ====

class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseListView(ListView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase-list')


# ==== VIEW SETS ====

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_id', 'user_id', 'order_date', 'total_price', 'quantity']
