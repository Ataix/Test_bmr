import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


client = APIClient()
User = get_user_model()


class TestAuthViews(TestCase):
    """
    Test if JWT auth
    """
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user_1', password='<PASSWORD>'
        )
        refresh = RefreshToken.for_user(self.test_user)
        self.auth = {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_order_list_valid_access(self):
        response = client.get(
            '/api/v1/order/list/',
            **self.auth
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_list_invalid_access(self):
        response = client.get(
            '/api/v1/order/list/',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_product_create_valid_access(self):
        response = client.post(
            f'/api/v1/product/create/',
            **self.auth
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_product_create_invalid_access(self):
        response = client.post(
            f'/api/v1/product/create/',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_product_list_anonymous_access(self):
        response = client.get(
            f'/api/v1/product/list/',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
