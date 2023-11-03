from django.test import TestCase

from products.models import Category, Product
from products.serializer import CategorySerializer, ProductSerializer


class CategorySerializerTestCase(TestCase):
    def test_serializer(self):
        category = Category.objects.create(slug='trousers', title='Брюки', gender='man')
        data = CategorySerializer([category], many=True).data
        expected_data = [
            {'title': 'Брюки'},
        ]
        self.assertEqual(expected_data, data)


class ProductSerializerTestCase(TestCase):
    def test_serializer(self):
        category = Category.objects.create(slug='accessories', title='Аксессуары', gender='woman')
        product = Product.objects.create(slug='wristwatch', title='Наручные часы', description='', category=category,
                                         available=True, number_of_sold=1, price=14000)
        data = ProductSerializer([product], many=True).data
        expected_data = [
            {'title': 'Наручные часы',
             'description': '',
             'category': 'Аксессуары',
             'available': True,
             'price': 14000,
             'discount': None,
             'photos': []}
        ]
        self.assertEqual(expected_data, data)
