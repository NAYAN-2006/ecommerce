from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Category, Subcategory, Product
from .serializers import (
    CategorySerializer, SubcategorySerializer, 
    ProductSerializer, ProductListSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Get all products in a category"""
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['category', 'name']

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        """Get all products in a subcategory"""
        subcategory = self.get_object()
        products = Product.objects.filter(subcategory=subcategory)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'subcategory', 'in_stock']
    search_fields = ['name', 'description', 'tags__tag']
    ordering_fields = ['name', 'price', 'rating', 'reviews_count', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.prefetch_related('images', 'features', 'tags').all()
        
        # Price range filter
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        # Rating filter
        min_rating = self.request.query_params.get('min_rating')
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        
        # Tag filter
        tags = self.request.query_params.get('tags')
        if tags:
            tag_list = [tag.strip() for tag in tags.split(',')]
            queryset = queryset.filter(tags__tag__in=tag_list).distinct()
        
        return queryset

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products (high rating and reviews)"""
        featured_products = Product.objects.filter(
            rating__gte=4.0,
            reviews_count__gte=100
        ).order_by('-rating', '-reviews_count')[:10]
        serializer = ProductListSerializer(featured_products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def on_sale(self, request):
        """Get products that are on sale (have original_price > price)"""
        on_sale_products = Product.objects.filter(
            original_price__gt=models.F('price')
        ).order_by('-created_at')
        serializer = ProductListSerializer(on_sale_products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Advanced search with multiple criteria"""
        query = request.query_params.get('q', '')
        category = request.query_params.get('category')
        subcategory = request.query_params.get('subcategory')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        min_rating = request.query_params.get('min_rating')
        in_stock = request.query_params.get('in_stock')
        
        queryset = Product.objects.all()
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(tags__tag__icontains=query)
            ).distinct()
        
        if category:
            queryset = queryset.filter(category__name=category)
        
        if subcategory:
            queryset = queryset.filter(subcategory__name=subcategory)
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        
        if in_stock == 'true':
            queryset = queryset.filter(in_stock=True)
        
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data) 