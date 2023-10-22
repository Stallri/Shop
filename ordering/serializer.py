from rest_framework import serializers

from .models import Order
from cart.models import CartProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'id', 'city', 'address', 'created', 'updated', 'paid')
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'paid': {'read_only': True}
        }

    def create(self, validated_data):
        city = validated_data.get('city')
        address = validated_data.get('address')
        user = self.context.get('user')
        order = Order.objects.create(user=user, city=city, address=address)
        cart_products = CartProduct.objects.filter(buyer=self.context.get('user'))
        for cp in cart_products:
            cp.order = order
            cp.save()
        return order
