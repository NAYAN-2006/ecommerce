from rest_framework import serializers
from .models import Category, Subcategory, Product, ProductImage, ProductFeature, ProductTag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'description', 'created_at', 'updated_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'alt_text', 'order']


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'feature', 'order']


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ['id', 'tag']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    features = ProductFeatureSerializer(many=True, read_only=True)
    tags = ProductTagSerializer(many=True, read_only=True)
    discount_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'original_price', 
            'category', 'subcategory', 'rating', 'reviews_count', 
            'main_image', 'in_stock', 'stock_count', 'images', 
            'features', 'tags', 'discount_percentage', 'created_at', 'updated_at'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    discount_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'original_price', 'category', 
            'subcategory', 'rating', 'reviews_count', 'main_image', 
            'in_stock', 'stock_count', 'discount_percentage'
        ] 