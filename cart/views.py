from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartProduct
from .serializer import CartProductSerializer
from products.models import Product


@permission_classes([IsAuthenticated])
class CartAPIView(APIView):
    def get(self, request):
        queryset = CartProduct.objects.filter(buyer=request.user.id)
        serializer = CartProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class CartAddAPIView(APIView):
    def post(self, request, slug):
        product = Product.objects.get(slug=slug)
        user = request.user
        cart_product = CartProduct.objects.create(buyer=user, product=product)
        data = {'user': cart_product.buyer.email, 'product': cart_product.product.title}
        return Response(data=data)
