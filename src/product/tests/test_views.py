import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Product, Review
from ..serializers import ProductSerializer


client = APIClient()
User = get_user_model()


class TestProductListView(TestCase):
    """
    Test product's list view
    """
    def setUp(self):
        Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=100.0,
            quantity=10,
        )
        Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category='Test Category 2',
            price=1088.0,
            quantity=1,
        )

    def test_list_view(self):
        response = client.get('/api/v1/product/list/')
        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProductDetailView(TestCase):
    """
    Test product's detail view
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category='Test Category 2',
            price=1243.3,
            quantity=31,
        )
        self.product_3 = Product.objects.create(
            name='Test Product 3',
            description='Test Description 3',
            category='Test Category 3',
            price=9902.4,
            quantity=95,
        )

    def test_valid_detail_view(self):
        response = client.get(f'/api/v1/product/{self.product_2.pk}/')
        product = Product.objects.get(pk=self.product_2.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_detail_view(self):
        response = client.get(f'/api/v1/product/{30}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestCaseBase(APITestCase):
    """
    Creating auth token for further testing
    """
    @property
    def bearer_token(self):
        self.test_user = User.objects.create_user(
            username='test_user', password='12345678'
        )
        refresh = RefreshToken.for_user(self.test_user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class TestProductCreateView(TestCaseBase):
    """
    Test product's create view
    """
    def setUp(self):
        self.valid_payload = {
            'name': 'Test Product 1',
            'description': 'Test Description 1',
            'category': 'Test Category 1',
            'price': 10340.7,
            'quantity': 13,
        }
        self.invalid_payload = {
            'name': '',
            'description': '',
            'category': '',
            'price': -1,
            'quantity': -1,
        }

    def test_valid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/create/',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/create/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestProductUpdateView(TestCaseBase):
    """
    Test product's update view (put, patch)
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category='Test Category 1',
            price=1243.3,
            quantity=31,
        )
        self.valid_payload_put = {
            'name': 'Edited Product',
            'description': 'Edited Descr',
            'category': 'Edited Category',
            'price': 10.8,
            'quantity': 1,
        }
        self.invalid_payload_put = {
            'name': '',
            'description': '',
            'category': '',
            'price': -1,
            'quantity': -1,
        }
        self.valid_payload_patch = {
            'price': 10.8,
            'quantity': 1,
        }
        self.invalid_payload_patch = {
            'price': '',
            'quantity': '',
        }

    def test_valid_put(self):
        response = self.client.put(
            f'/api/v1/product/{self.product_1.pk}/',
            data=json.dumps(self.valid_payload_put),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put(self):
        response = self.client.put(
            f'/api/v1/product/{self.product_1.pk}/',
            data=json.dumps(self.invalid_payload_put),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_patch(self):
        response = self.client.patch(
            f'/api/v1/product/{self.product_2.pk}/',
            data=json.dumps(self.valid_payload_patch),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_patch(self):
        response = self.client.patch(
            f'/api/v1/product/{self.product_2.pk}/',
            data=json.dumps(self.invalid_payload_patch),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestProductDeleteView(TestCaseBase):
    """
    Test product's delete view
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=10340.7,
            quantity=1,
        )
        self.product_2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category='Test Category 1',
            price=1243.3,
            quantity=31,
        )

    def test_valid_delete(self):
        response = self.client.delete(
            f'/api/v1/product/{self.product_1.pk}/',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = self.client.delete(
            f'/api/v1/product/{0}/',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestReviewCreateView(TestCaseBase):
    """
    Review's creation view testing
    """
    def setUp(self):
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=10340.7,
            quantity=1,
        )
        self.valid_payload = {
            'product': self.product_1.id,
            'text': 'Test Description 1',
            'author': 1,
            'rate': 5,
        }
        self.invalid_payload = {
            'product': '',
            'text': 'Test Description 1',
            'author': 1,
            'rate': 6,
        }

    def test_valid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/{self.product_1.id}/reviews/',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_view(self):
        response = self.client.post(
            f'/api/v1/product/{self.product_1.id}/reviews/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestReviewUpdateView(TestCaseBase):
    """
    Test review's update view (put, patch)
    """
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user_1', password='<PASSWORD>'
        )
        self.product_1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category='Test Category 1',
            price=10340.7,
            quantity=1,
        )
        self.review_1 = Review.objects.create(
            product=self.product_1,
            text='Test text',
            author=self.test_user,
            rate=5,
        )
        self.valid_payload = {
            'text': 'Edited',
            'rate': 3,
        }

    def test_valid(self):
        response = self.client.patch(
            f'/api/v1/product/{self.product_1.pk}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestReviewDeleteView(TestCaseBase):
    """
    Review's delete view testing
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
            price=10340.7,
            quantity=1,
        )
        self.review_1 = Review.objects.create(
            product=self.product_1,
            text='Test text',
            author=self.test_user,
            rate=5,
        )
        self.review_2 = Review.objects.create(
            product=self.product_1,
            text='Test text',
            author=self.test_user,
            rate=5,
        )

    def test_valid(self):
        response = self.client.delete(
            f'/api/v1/product/{self.product_1.pk}/reviews/',
            **self.auth,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_valid_forbidden(self):
        response = self.client.delete(
            f'/api/v1/product/{self.product_1.pk}/reviews/',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid(self):
        response = self.client.patch(
            f'/api/v1/product/{30}/reviews/',
            **self.bearer_token,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
