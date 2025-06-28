from django.contrib import admin
from .models import Cart, CartItem, Wishlist, WishlistItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'total_items', 'total_price')
    inlines = [CartItemInline]
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'created_at')
    search_fields = ('cart__user__username', 'product__name')

class WishlistItemInline(admin.TabularInline):
    model = WishlistItem
    extra = 0

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    inlines = [WishlistItemInline]
    search_fields = ('user__username',)

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'created_at')
    search_fields = ('wishlist__user__username', 'product__name') 