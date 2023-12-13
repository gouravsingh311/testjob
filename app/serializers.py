from rest_framework import serializers
from django.utils import timezone
from .models import Customer, Product, Order, OrderItem

def validate_positive_decimal(value):
    if value < 0:
        raise serializers.ValidationError("Value must be a positive decimal.")

def validate_max_weight(value):
    if value > 25:
        raise serializers.ValidationError("Weight must not be more than 25kg.")

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    """
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_name(self, value):
        """
        Validate that the customer name is unique.
        """
        if Customer.objects.filter(name=value).exists():
            raise serializers.ValidationError("Customer with this name already exists.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        """
        Validate that the product name is unique.
        """
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product with this name already exists.")
        return value

    def validate_weight(self, value):
        """
        Validate the product weight is a positive decimal and not more than 25kg.
        """
        validate_positive_decimal(value)
        validate_max_weight(value)
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_order_date(self, value):
        """
        Validate that the order date is not in the past.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value

    def validate(self, data):
        """
        Validate the cumulative weight of order items is under 150kg.
        """
        order_items = data.get('order_item', [])
        total_weight = sum(item['product'].weight * item['quantity'] for item in order_items)
        if total_weight > 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")
        return data

    def create(self, validated_data):
        """
        Create an Order object along with associated OrderItem objects.
        """
        order_items_data = validated_data.pop('order_item', [])
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)

        
