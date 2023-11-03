from rest_framework import serializers

from .models import CartProduct
from products.serializer import ProductSerializer


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ('product',)
