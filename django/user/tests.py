from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .views import UserViewSet
from .models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 30,
        }

    def test_user_creation(self):
        user = User.objects.create(
            first_name=self.user_data['first_name'],
            last_name=self.user_data['last_name'],
            age=self.user_data['age'],
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.age, self.user_data['age'])


class UserViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.age, 25)

    def test_get_user_detail(self):
        user = User.objects.create(first_name='John', last_name='Doe', age=25)
        url = reverse('user-detail', args=[user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')
        self.assertEqual(response.data['age'], 25)

    def test_delete_user(self):
        user = User.objects.create(first_name='John', last_name='Doe', age=25)
        url = reverse('user-detail', args=[user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)



