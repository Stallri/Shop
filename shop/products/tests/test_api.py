from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from products.models import Category, Product
from products.serializer import CategorySerializer, ProductSerializer


class CategoryAPITestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(slug='hats', title='Головные уборы', gender='man')
        url = reverse('category_list', kwargs={'gender': 'man'})
        response = self.client.get(url)
        serializer = CategorySerializer([category], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data['results'])


class ProductListAPITestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(slug='socks', title='Носки', gender='man')
        product = Product.objects.create(slug='sport-socks', title='Спортивные носки', description='description',
                                         category=category, available=True, price=1000)
        url = reverse('product_list', kwargs={'category': 'socks'})
        response = self.client.get(url)
        serializer = ProductSerializer([product], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data['results'])


class ProductAPITestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(slug='outerwear', title='Верхняя одежда', gender='boy')
        product = Product.objects.create(slug='puffer', title='Пуховик', description='',
                                         category=category, available=True, price=10000)
        url = reverse('product_detail', kwargs={'slug': 'puffer'})
        response = self.client.get(url)
        serializer = ProductSerializer(product)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)


class PopularProductsAPITestCase(APITestCase):
    def test_get(self):
        category1 = Category.objects.create(slug='outerwear', title='Верхняя одежда', gender='boy')
        category2 = Category.objects.create(slug='socks', title='Носки', gender='man')
        category3 = Category.objects.create(slug='hats', title='Головные уборы', gender='man')
        product1 = Product.objects.create(slug='puffer', title='Пуховик', description='',
                                          category=category1, number_of_sold=3, available=True, price=10000)
        product2 = Product.objects.create(slug='sport-socks', title='Спортивные носки', description='description',
                                          category=category2, number_of_sold=2, available=True, price=1000)
        product3 = Product.objects.create(slug='baseball-cap', title='Бейсболка', description='',
                                          category=category3, number_of_sold=1, available=True, price=1500)
        url = reverse('popular_products')
        response = self.client.get(url)
        serializer = ProductSerializer([product1, product2, product3], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data['results'])
