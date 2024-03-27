from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


class OrderItem(models.Model):
    """
    Represents items (products) in the order.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product} {self.price}'


class Order(models.Model):
    """
    Represents an order build by users
    """
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return f'{self.user} {self.items}'
