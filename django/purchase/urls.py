from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('list', PurchaseListView.as_view(), name='purchase-list'),
    path('detail/<int:id>', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('create', PurchaseCreateView.as_view(), name='purchase-form')
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
