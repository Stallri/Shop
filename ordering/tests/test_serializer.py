from django.test import TestCase

from account.models import User
from ordering.models import Order
from ordering.serializer import OrderSerializer
from datetime import datetime


class OrderSerializerTestCase(TestCase):
    def test_serializer(self):
        user = User.objects.create(email='123@gmail.com', password='1234')
        order = Order.objects.create(user=user, city='city', address='address')
        data = OrderSerializer(order).data
        expected_data = {
            'user': 1,
            'id': 1,
            'city': 'city',
            'address': 'address',
            'created': order.created.strftime('%H:%M %d-%m-%Y'),
            'updated': order.updated.strftime('%H:%M %d-%m-%Y'),
            'paid': False,
        }
        self.assertEqual(expected_data, data)
