from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category


class CategoryAPIList(ListAPIView):
    # Вывод списка категорий
    serializer_class = CategorySerializer

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        return Category.objects.filter(gender=gender)


class ProductAPIList(ListAPIView):
    # Вывод списка товаров
    serializer_class = ProductSerializer

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        category = self.kwargs.get('category')
        return Product.objects.filter(gender=gender, category__title=category)


class ProductAPI(RetrieveAPIView):
    # Вывод одного товара
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.get(slug=slug)
