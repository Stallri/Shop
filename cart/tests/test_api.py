from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from products.models import Product, Category
from account.models import User
from cart.models import CartProduct
from cart.serializer import CartProductSerializer


class CartAPITestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(slug='suits', title='Костюмы', gender='man')
        product = Product.objects.create(slug='smoking', title='Смокинг', description='description',
                                         category=category, available=True, price=20000)
        url_register = reverse('registration')
        data_register = {
            'email': 'test1@gmail.com',
            'password': '1111',
            'password2': '1111'
        }
        response_register = self.client.post(url_register, data_register, format='json')
        url_token = reverse('token_obtain_pair')
        data_token = {
            'email': 'test1@gmail.com',
            'password': '1111'
        }
        response_token = self.client.post(url_token, data_token, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_token.data['access'])
        cart_product = CartProduct.objects.create(product=product, buyer=User.objects.get(email='test1@gmail.com'))
        url_cart = reverse('cart_list')
        response_cart = self.client.get(url_cart)
        serializer = CartProductSerializer([cart_product], many=True)
        self.assertEqual(status.HTTP_200_OK, response_cart.status_code)
        self.assertEqual(serializer.data + [{'total_price': 20000}], response_cart.data)


class CartAddAPITestCase(APITestCase):
    def test_post(self):
        category = Category.objects.create(slug='shoes', title='Обувь', gender='man')
        product = Product.objects.create(slug='sneakers', title='Кроссовки', description='description',
                                         category=category, available=True, price=12000)
        url_register = reverse('registration')
        data_register = {
            'email': 'test2@gmail.com',
            'password': '1111',
            'password2': '1111'
        }
        response_register = self.client.post(url_register, data_register, format='json')
        url_token = reverse('token_obtain_pair')
        data_token = {
            'email': 'test2@gmail.com',
            'password': '1111'
        }
        response_token = self.client.post(url_token, data_token, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_token.data['access'])
        url = reverse('cart_add', kwargs={'slug': 'sneakers'})
        expected_data = {
            'user': 'test2@gmail.com',
            'product': 'Кроссовки'
        }
        response_cart = self.client.post(url)
        self.assertEqual(expected_data, response_cart.data)
