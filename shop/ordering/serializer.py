from rest_framework import serializers

from account.models import User
from cart.serializer import CartProductSerializer
from .models import Order
from cart.models import CartProduct


class OrderSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'city', 'address', 'created', 'total_price', 'products', 'paid')
        extra_kwargs = {
            'id': {'read_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'paid': {'read_only': True}
        }
        depth = 1

    def create(self, validated_data):
        city = validated_data.get('city')
        address = validated_data.get('address')
        user = self.context.get('user')
        order = Order.objects.create(user=user, city=city, address=address)
        cart_products = CartProduct.objects.filter(buyer=self.context.get('user'))
        for cp in cart_products:
            cp.order = order
            if cp.product.discount:
                order.total_price += (cp.product.price - ((cp.product.discount.percent / 100) * cp.product.price))
            else:
                order.total_price += cp.product.price
            order.save()
            cp.save()
        return order
