from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ordering.models import Order
from account.models import User
from ordering.serializer import OrderSerializer


class OrderingAPICase(APITestCase):

    def setUp(self):
        self.url_register = reverse('registration')
        self.data_register = {
            'email': 'test5@gmail.com',
            'password': '1111',
            'password2': '1111'
        }
        self.response_register = self.client.post(self.url_register, self.data_register, format='json')
        url_token = reverse('token_obtain_pair')
        data_token = {
            'email': 'test5@gmail.com',
            'password': '1111'
        }
        response_token = self.client.post(url_token, data_token, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_token.data['access'])
        self.user = User.objects.get(email='test5@gmail.com')
        self.order_url = reverse('ordering')

    def test_get(self):
        order = Order.objects.create(user=self.user, city='city', address='address')

        response = self.client.get(self.order_url)
        serializer = OrderSerializer(self.user.orders, many=True)
        self.assertEqual(serializer.data, response.data)

    def test_post(self):
        order_data = {
            'city': 'city',
            'address': 'address'
        }
        response = self.client.post(self.order_url, data=order_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(Order.objects.count(), 1)

    def test_post_error(self):
        order_data = {
            'user': self.user.email,
            'city': 'city',
            'address': 'address'
        }
        Order.objects.create(user=self.user, city='city', address='address')
        response = self.client.post(self.order_url, data=order_data, format='json')
        self.assertEqual({'error': 'Order not paid'}, response.data)

    def test_delete(self):
        Order.objects.create(user=self.user, city='city', address='address')
        response = self.client.delete(self.order_url)
        self.assertEqual(Order.objects.count(), 0)

    def test_delete_error(self):
        Order.objects.create(user=self.user, city='city', address='address', paid=True)
        response = self.client.delete(self.order_url)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual({'error': 'No unpaid order'}, response.data)
