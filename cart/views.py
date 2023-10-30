from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import CartProduct
from .serializer import CartProductSerializer
from products.models import Product


@permission_classes([IsAuthenticated])
class CartAPIView(APIView):
    def get(self, request):
        queryset = CartProduct.objects.all().select_related('product')
        serializer = CartProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class CartAddAPIView(APIView):
    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        user = request.user
        cart_product = CartProduct.objects.create(buyer=user, product=product)
        product.number_of_sold += 1
        product.save()
        return Response(CartProductSerializer(instance=CartProduct.objects.all(), many=True).data)
