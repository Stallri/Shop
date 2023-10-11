from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializer import ProductSerializer
from .models import Product


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
        gender = self.kwargs.get('gender')
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')
        return Product.objects.get(gender=gender, category__title=category, slug=slug)
