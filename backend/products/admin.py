from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage, ProductFeature, ProductTag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 0

class ProductTagInline(admin.TabularInline):
    model = ProductTag
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price', 'in_stock', 'stock_count', 'created_at')
    search_fields = ('name', 'category__name', 'subcategory__name')
    list_filter = ('category', 'subcategory', 'in_stock')
    inlines = [ProductImageInline, ProductFeatureInline, ProductTagInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_url', 'order')
    search_fields = ('product__name',)

@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature', 'order')
    search_fields = ('product__name', 'feature')

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('product', 'tag')
    search_fields = ('product__name', 'tag') 