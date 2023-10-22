from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializer import OrderSerializer


@permission_classes([IsAuthenticated])
class OrderAPI(APIView):
    def get(self, request):
        queryset = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if (request.user.orders.first()) and (not request.user.orders.first().paid):
            return Response({'message': 'Order not paid'})
        serializer = OrderSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        Order.objects.filter(user=request.user).first().delete()
        return Response({'message': 'Order was delete'})
