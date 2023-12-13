from django.urls import path
from .views import CustomerListCreateView, ProductListCreateView, OrderListCreateView, OrderDetailView

urlpatterns = [
    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
