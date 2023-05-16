from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('<int:id>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create/', PurchaseCreateView.as_view(), name='purchase-form')
]