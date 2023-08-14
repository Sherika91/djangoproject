from catalog.models import Category, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command for filling database with data."""
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_list = [
            {'category': 'Headphones', 'description': 'Headphones description'},
            {'category': 'Smartphones', 'description': 'Smartphones description'},
        ]

        products = [
            {'name': 'Sony wh-1000xm4', 'description': 'Sony wh-1000xm4 description',
             'category': 'Headphones', 'price': 600},
            {'name': 'Air Pods Pro 2', 'description': 'Air Pods Pro 2 description',
             'category': 'Headphones', 'price': 400},
            {'name': 'iPhone 12', 'description': 'iPhone 12 description',
             'category': 'Smartphones', 'price': 1000},
            {'name': 'iPhone 11', 'description': 'iPhone 11 description',
             'category': 'Smartphones', 'price': 700},
            {'name': 'Samsung Galaxy S21', 'description': 'Samsung Galaxy S21 description',
             'category': 'Smartphones', 'price': 800},
        ]

        # Categories creation.
        categories_to_create = []
        for category in categories_list:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)
        print('Categories Created!')

        # Products creation.
        products_to_create = []
        for product in products:
            products_to_create.append(Product(**product))

        Product.objects.bulk_create(products_to_create)
        print('Products Added!')
