from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Product, Order, OrderItem
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Customer objects.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Product objects.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Order objects.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Order object.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
