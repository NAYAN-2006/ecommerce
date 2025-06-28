from rest_framework import serializers
from .models import Address, Order, OrderItem
from products.serializers import ProductListSerializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'full_name', 'phone_number', 'address_line1', 'address_line2',
            'city', 'state', 'zip_code', 'country', 'is_default', 'created_at', 'updated_at'
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'address', 'status', 'total_price', 'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'status', 'total_price', 'created_at', 'updated_at', 'items']

class CreateOrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class CreateOrderSerializer(serializers.Serializer):
    address_id = serializers.IntegerField()
    items = CreateOrderItemSerializer(many=True) 