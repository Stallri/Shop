from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartProduct
from .serializer import CartProductSerializer


class CartAPIView(APIView):
    def get(self, request):
        queryset = CartProduct.objects.filter(buyer=request.user.id)
        print(request.user)
        serializer = CartProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)
