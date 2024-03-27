from django.contrib.auth import get_user_model
from django.test import TestCase

from order.models import Order, OrderItem
from product.models import Product

User = get_user_model()


class TestOrderModel(TestCase):
    """
    Test product's model
    """
    def setUp(self):
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
            user=self.user_1,
            address='Test Address 1',
            comment='Test Comment',
            total=322.0,
            discount=0,
        )
        self.order.items.set([self.order_item_1, self.order_item_2])

    def test_order_creation(self):
        user = User.objects.get(username='user1')
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(self.order.user, user)
        self.assertEqual(self.order.items, order.items)
        self.assertEqual(self.order.total, order.total)
