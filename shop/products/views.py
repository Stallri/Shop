from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category


class CategoryListAPI(ListAPIView):
    # Вывод списка категорий
    serializer_class = CategorySerializer

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        return Category.objects.filter(gender=gender)


class ProductListAPI(ListAPIView):
    # Вывод списка товаров категории
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Product.objects.filter(category__slug=category)


class PopularProductsAPI(ListAPIView):
    # Вывод списка наиболее часто покупаемых товаров
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.order_by('-number_of_sold')[:3]
        return queryset


class ProductAPI(RetrieveAPIView):
    # Вывод одного товара
    serializer_class = ProductSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Product.objects.get(slug=slug)
