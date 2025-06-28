from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Address, Order, OrderItem
from products.models import Product
from .serializers import (
    AddressSerializer, OrderSerializer, CreateOrderSerializer
)

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = get_object_or_404(Address, id=serializer.validated_data['address_id'], user=request.user)
        items_data = serializer.validated_data['items']
        total_price = 0
        order_items = []
        for item in items_data:
            product = get_object_or_404(Product, id=item['product_id'])
            quantity = item['quantity']
            price = product.price * quantity
            total_price += price
            order_items.append({'product': product, 'quantity': quantity, 'price': product.price})
        order = Order.objects.create(user=request.user, address=address, total_price=total_price)
        for item in order_items:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED) 