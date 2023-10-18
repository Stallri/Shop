from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from account.models import Profile, User
from account.serializer import ProfileSerializer


class ProfileAPITestCase(APITestCase):
    def setUp(self):
        self.url_register = reverse('registration')
        self.data_register = {
            'email': 'test3@gmail.com',
            'password': '1111',
            'password2': '1111'
        }
        self.response_register = self.client.post(self.url_register, self.data_register, format='json')
        self.profile_data = {
            'user_name': 'changed_user_name',
            'phone_number': '+722222222',
            'user': 'test3@gmail.com'
        }
        url_token = reverse('token_obtain_pair')
        data_token = {
            'email': 'test3@gmail.com',
            'password': '1111'
        }
        response_token = self.client.post(url_token, data_token, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_token.data['access'])
        self.user = User.objects.get(email='test3@gmail.com')
        self.profile = Profile.objects.get(user=self.user)
        self.profile.user_name = 'test_user_name'
        self.profile.phone_number = '+711111111'
        self.profile.save()

    def test_get(self):
        url = reverse('profile')
        response = self.client.get(url)
        serializer = ProfileSerializer(self.profile)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_put(self):
        url = reverse('profile')
        response = self.client.put(url, data=self.profile_data)
        changed_user = User.objects.get(email='test3@gmail.com')
        serializer = ProfileSerializer(changed_user.profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)
