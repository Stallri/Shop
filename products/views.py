from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializer import ProductSerializer
from .models import Product


class ProductAPIList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
