from rest_framework import serializers

from .models import User, Profile
from .tasks import registration_mail


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(email=validated_data.get('email'))
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError({'error': 'passwords don`t match'})

        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        registration_mail.delay(user.email)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ('user_name', 'phone_number', 'user')
