from rest_framework import serializers

from .models import Product, Category
from discounts.serializer import DiscountSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    discount = DiscountSerializer()

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'available', 'price', 'discount', 'photos')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
