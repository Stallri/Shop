from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegistrationSerializer, ProfileSerializer
from .models import User, Profile


# class UserAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class ProfileAPIView(APIView):
    def get(self, request):
        serializer = ProfileSerializer(instance=request.user.profile)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProfileSerializer(data=request.data, instance=request.user.profile)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):
        serializer = ProfileSerializer(data=request.data, instance=request.user.profile, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
