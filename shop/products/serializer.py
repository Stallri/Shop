from rest_framework import serializers

from .models import Product, Category, ProductPhoto
from discounts.serializer import DiscountSerializer


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('photo',)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    discount = DiscountSerializer()
    photos = ProductPhotoSerializer(many=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        if instance.discount:
            return instance.price - instance.price * (instance.discount.percent / 100)
        return instance.price

    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'available', 'price', 'discount', 'photos')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
