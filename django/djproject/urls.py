from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('books/', include('book.urls')),
    path('purchases/', include('purchase.urls')),
]





