from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'available', 'number_of_sold', 'price', 'photos')
        extra_kwargs = {'number_of_sold': {'read_only': True}}
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
