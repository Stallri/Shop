from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category


@extend_schema(tags=["Shop"])
@extend_schema(summary="Получить список категорий")
class CategoryListAPI(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        gender = self.kwargs.get('gender')
        return Category.objects.filter(gender=gender)


@extend_schema(tags=["Shop"])
@extend_schema(summary="Получить список товаров")
class ProductListAPI(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Product.objects.filter(category__slug=category)


@extend_schema(tags=["Shop"])
@extend_schema(summary="Получить список наиболее часто покупаемых товаров")
class PopularProductsAPI(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.order_by('-number_of_sold')[:3]
        return queryset


@extend_schema(tags=["Shop"])
@extend_schema(summary="Получить конкретный товар")
class ProductAPI(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Product.objects.get(slug=slug)
