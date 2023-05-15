from django.urls import path
from .views import PurchaseListView, PurchaseDetailView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchases'),
    path('<int:id>', PurchaseDetailView.as_view(), name='purchase_id')
]