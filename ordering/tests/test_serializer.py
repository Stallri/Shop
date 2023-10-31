from collections import OrderedDict

from django.test import TestCase

from account.models import User
from cart.models import CartProduct
from discounts.models import Discount
from ordering.models import Order
from ordering.serializer import OrderSerializer
from datetime import datetime, timedelta
from django.utils import timezone

from products.models import Product, Category


class OrderSerializerTestCase(TestCase):
    def test_serializer(self):
        discount = Discount.objects.create(percent=60, start=datetime.now(tz=timezone.utc),
                                           end=(datetime.now(tz=timezone.utc) + timedelta(days=4)))
        category = Category.objects.create(slug='suits', title='Костюмы', gender='man')
        product = Product.objects.create(slug='smoking', title='Смокинг', description='description',
                                         category=category, available=True, discount=discount, price=20000)
        user = User.objects.create(email='123@gmail.com', password='1234')
        cart_product = CartProduct.objects.create(product=product, buyer=user)
        serializer = OrderSerializer(data={'city': 'city', 'address': 'address'}, context={'user': user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        order = Order.objects.first()
        expected_data = {
            'id': 1,
            'user': '123@gmail.com',
            'city': 'city',
            'address': 'address',
            'created': order.created.strftime('%H:%M %d-%m-%Y'),
            'total_price': 8000,
            'products': [OrderedDict([('product', OrderedDict(
                [('title', 'Смокинг'), ('description', 'description'), ('category', 'Костюмы'), ('available', True),
                 ('price', 20000),
                 ('discount', OrderedDict([('percent', 60),
                                           ('start', discount.start.strftime('%H:%M %d-%m-%Y')),
                                           ('end', discount.end.strftime('%H:%M %d-%m-%Y'))])), ('photos', [])]))])],
            'paid': False
        }
        self.assertEqual(expected_data, data)
