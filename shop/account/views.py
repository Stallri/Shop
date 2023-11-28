from drf_spectacular.utils import extend_schema
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegistrationSerializer, ProfileSerializer
from .models import User, Profile


@extend_schema(tags=["Registration"])
class RegistrationAPIView(APIView):
    @extend_schema(summary="Регистрация пользователя")
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@extend_schema(tags=["Profile"])
@permission_classes([IsAuthenticated])
class ProfileAPIView(APIView):
    @extend_schema(summary="Получение профиля")
    def get(self, request):
        serializer = ProfileSerializer(instance=request.user.profile)
        return Response(serializer.data)

    @extend_schema(summary="Изменение профиля")
    def put(self, request):
        serializer = ProfileSerializer(data=request.data, instance=request.user.profile)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
