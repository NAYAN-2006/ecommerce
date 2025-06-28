from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Category, Subcategory, Product, ProductImage, ProductFeature, ProductTag
from decimal import Decimal


class Command(BaseCommand):
    help = 'Load sample data for the e-commerce application'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create categories
        electronics, _ = Category.objects.get_or_create(
            name='Electronics',
            defaults={'description': 'Electronic devices and accessories'}
        )
        
        clothing, _ = Category.objects.get_or_create(
            name='Clothing',
            defaults={'description': 'Fashion and apparel'}
        )
        
        home_garden, _ = Category.objects.get_or_create(
            name='Home & Garden',
            defaults={'description': 'Home improvement and garden supplies'}
        )
        
        sports, _ = Category.objects.get_or_create(
            name='Sports & Outdoors',
            defaults={'description': 'Sports equipment and outdoor gear'}
        )

        # Create subcategories
        audio, _ = Subcategory.objects.get_or_create(
            name='Audio',
            category=electronics,
            defaults={'description': 'Audio equipment and accessories'}
        )
        
        wearables, _ = Subcategory.objects.get_or_create(
            name='Wearables',
            category=electronics,
            defaults={'description': 'Smartwatches and fitness trackers'}
        )
        
        accessories, _ = Subcategory.objects.get_or_create(
            name='Accessories',
            category=electronics,
            defaults={'description': 'Electronic accessories'}
        )
        
        tops, _ = Subcategory.objects.get_or_create(
            name='Tops',
            category=clothing,
            defaults={'description': 'Shirts, t-shirts, and tops'}
        )
        
        kitchen, _ = Subcategory.objects.get_or_create(
            name='Kitchen',
            category=home_garden,
            defaults={'description': 'Kitchen appliances and utensils'}
        )
        
        fitness, _ = Subcategory.objects.get_or_create(
            name='Fitness',
            category=sports,
            defaults={'description': 'Fitness equipment and accessories'}
        )

        # Create products
        products_data = [
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': 'Premium wireless headphones with noise cancellation, 30-hour battery life, and crystal-clear sound quality.',
                'price': Decimal('89.99'),
                'original_price': Decimal('129.99'),
                'category': electronics,
                'subcategory': audio,
                'rating': Decimal('4.5'),
                'reviews_count': 1247,
                'main_image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop',
                'stock_count': 45,
                'features': [
                    'Active Noise Cancellation',
                    '30-hour battery life',
                    'Bluetooth 5.0',
                    'Built-in microphone',
                    'Foldable design'
                ],
                'tags': ['wireless', 'bluetooth', 'noise-cancelling', 'audio'],
                'images': [
                    'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400&h=400&fit=crop'
                ]
            },
            {
                'name': 'Smart Fitness Watch',
                'description': 'Advanced fitness tracking with heart rate monitoring, GPS, and 7-day battery life.',
                'price': Decimal('199.99'),
                'original_price': Decimal('249.99'),
                'category': electronics,
                'subcategory': wearables,
                'rating': Decimal('4.3'),
                'reviews_count': 892,
                'main_image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop',
                'stock_count': 23,
                'features': [
                    'Heart rate monitoring',
                    'GPS tracking',
                    '7-day battery life',
                    'Water resistant',
                    'Sleep tracking'
                ],
                'tags': ['fitness', 'smartwatch', 'health', 'tracking'],
                'images': [
                    'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1544117519-31a4b719223d?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400&h=400&fit=crop'
                ]
            },
            {
                'name': 'Organic Cotton T-Shirt',
                'description': 'Comfortable and sustainable organic cotton t-shirt available in multiple colors.',
                'price': Decimal('24.99'),
                'original_price': Decimal('34.99'),
                'category': clothing,
                'subcategory': tops,
                'rating': Decimal('4.7'),
                'reviews_count': 2156,
                'main_image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
                'stock_count': 156,
                'features': [
                    '100% organic cotton',
                    'Sustainable production',
                    'Multiple colors available',
                    'Comfortable fit',
                    'Machine washable'
                ],
                'tags': ['organic', 'cotton', 'sustainable', 'comfortable'],
                'images': [
                    'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=400&h=400&fit=crop'
                ]
            },
            {
                'name': 'Stainless Steel Water Bottle',
                'description': 'Insulated stainless steel water bottle that keeps drinks cold for 24 hours or hot for 12 hours.',
                'price': Decimal('19.99'),
                'original_price': Decimal('29.99'),
                'category': home_garden,
                'subcategory': kitchen,
                'rating': Decimal('4.6'),
                'reviews_count': 3421,
                'main_image': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&h=400&fit=crop',
                'stock_count': 89,
                'features': [
                    '24-hour cold retention',
                    '12-hour hot retention',
                    'BPA-free',
                    'Leak-proof design',
                    '32oz capacity'
                ],
                'tags': ['insulated', 'stainless-steel', 'eco-friendly', 'bpa-free'],
                'images': [
                    'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1589365278144-9ea1db6c4b4c?w=400&h=400&fit=crop'
                ]
            },
            {
                'name': 'Yoga Mat Premium',
                'description': 'Premium non-slip yoga mat with alignment lines and eco-friendly materials.',
                'price': Decimal('49.99'),
                'original_price': Decimal('79.99'),
                'category': sports,
                'subcategory': fitness,
                'rating': Decimal('4.8'),
                'reviews_count': 1893,
                'main_image': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=400&fit=crop',
                'stock_count': 34,
                'features': [
                    '6mm thickness',
                    'Non-slip surface',
                    'Alignment lines',
                    'Eco-friendly materials',
                    'Includes carrying strap'
                ],
                'tags': ['yoga', 'fitness', 'non-slip', 'eco-friendly'],
                'images': [
                    'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1592432678016-e910b452f9a2?w=400&h=400&fit=crop',
                    'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=400&fit=crop'
                ]
            }
        ]

        for product_data in products_data:
            # Create product
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'original_price': product_data['original_price'],
                    'category': product_data['category'],
                    'subcategory': product_data['subcategory'],
                    'rating': product_data['rating'],
                    'reviews_count': product_data['reviews_count'],
                    'main_image': product_data['main_image'],
                    'stock_count': product_data['stock_count'],
                    'in_stock': True
                }
            )

            if created:
                # Add features
                for i, feature in enumerate(product_data['features']):
                    ProductFeature.objects.get_or_create(
                        product=product,
                        feature=feature,
                        defaults={'order': i}
                    )

                # Add tags
                for tag in product_data['tags']:
                    ProductTag.objects.get_or_create(
                        product=product,
                        tag=tag
                    )

                # Add images
                for i, image_url in enumerate(product_data['images']):
                    ProductImage.objects.get_or_create(
                        product=product,
                        image_url=image_url,
                        defaults={'order': i}
                    )

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data!')
        ) 