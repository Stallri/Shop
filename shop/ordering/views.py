from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializer import OrderSerializer


@extend_schema(tags=["Ordering"])
@permission_classes([IsAuthenticated])
class OrderAPI(APIView):
    @extend_schema(summary="Получение списка заказов")
    def get(self, request):
        queryset = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary="Создание заказа")
    def post(self, request):
        if (request.user.orders.first()) and (not request.user.orders.first().paid):
            return Response({'error': 'Order not paid'})
        serializer = OrderSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(summary="Удаление заказа")
    def delete(self, request):
        if (request.user.orders.first()) and (not request.user.orders.first().paid):
            Order.objects.filter(user=request.user).first().delete()
            return Response({'message': 'Order was delete'})
        return Response({'error': 'No unpaid order'})
