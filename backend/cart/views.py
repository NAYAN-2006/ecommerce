from rest_framework import status, generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, Wishlist, WishlistItem
from products.models import Product
from .serializers import (
    CartSerializer, CartItemSerializer, AddToCartSerializer, UpdateCartItemSerializer,
    WishlistSerializer, WishlistItemSerializer, AddToWishlistSerializer
)


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add(self, request):
        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        quantity = serializer.validated_data['quantity']
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()
        return Response({'message': 'Product added to cart.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def update_item(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        if int(quantity) <= 0:
            item.delete()
            return Response({'message': 'Item removed from cart.'}, status=status.HTTP_200_OK)
        item.quantity = quantity
        item.save()
        return Response({'message': 'Cart item updated.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def remove(self, request):
        product_id = request.data.get('product_id')
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        item.delete()
        return Response({'message': 'Item removed from cart.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def clear(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart.items.all().delete()
        return Response({'message': 'Cart cleared.'}, status=status.HTTP_200_OK)


class WishlistViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add(self, request):
        serializer = AddToWishlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Product, id=serializer.validated_data['product_id'])
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        item, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
        if not created:
            return Response({'message': 'Product already in wishlist.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Product added to wishlist.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def remove(self, request):
        product_id = request.data.get('product_id')
        wishlist = get_object_or_404(Wishlist, user=request.user)
        item = get_object_or_404(WishlistItem, wishlist=wishlist, product_id=product_id)
        item.delete()
        return Response({'message': 'Item removed from wishlist.'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def clear(self, request):
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.items.all().delete()
        return Response({'message': 'Wishlist cleared.'}, status=status.HTTP_200_OK) 