import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from order.models import OrderItem, Order
from order.serializers import OrderSerializer
from product.models import Product

client = APIClient()
User = get_user_model()


class TestOrderViews(TestCase):
    """
    Test product's list view
    """
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user_1', password='<PASSWORD>'
        )
        refresh = RefreshToken.for_user(self.test_user)
        self.auth = {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=322.0,
            quantity=10,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category='Test Category 2',
            price=3232.0,
            quantity=5,
        )
        self.order_item_1 = OrderItem.objects.create(
            product=self.product_1,
            quantity=1,
            price=322.0
        )
        self.order_item_2 = OrderItem.objects.create(
            product=self.product_2,
            quantity=4,
            price=32266.0
        )
        self.user_1 = User.objects.create(
            username='user1',
            password='<PASSWORD>'
        )
        self.order = Order.objects.create(
            user=self.test_user,
            address='Test Address 1',
            comment='Test Comment',
            total=322.0,
            discount=0,
        )
        self.order.items.set([self.order_item_1, self.order_item_2])

        self.order_create_valid_payload = {
            'user': self.test_user.pk,
            'address': 'Test Address 1',
            'comment': 'Test Comment 1',
            'total': 322.0,
            'discount': 0,
            'items': [
                {
                    'product': self.order_item_1.product.pk,
                    'quantity': self.order_item_1.quantity,
                    'price': self.order_item_1.price,
                }
            ]
        }
        self.order_create_invalid_payload = {
            'user': '',
            'address': '',
            'comment': 'Test Comment 1',
            'total': 322.0,
            'discount': 0,
            'items': ''
        }

    def test_list_view(self):
        response = client.get(
            '/api/v1/order/list/',
            **self.auth
        )
        orders = Order.objects.all().order_by('id')
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_view(self):
        response = client.get(
            f'/api/v1/order/{self.order.pk}/',
            **self.auth
        )
        order = Order.objects.get(pk=self.order.pk)
        serializer = OrderSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_view_valid(self):
        response = client.post(
            f'/api/v1/order/create/',
            data=json.dumps(self.order_create_valid_payload),
            content_type='application/json',
            **self.auth,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_view_invalid(self):
        response = client.post(
            f'/api/v1/order/create/',
            data=json.dumps(self.order_create_invalid_payload),
            content_type='application/json',
            **self.auth,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
