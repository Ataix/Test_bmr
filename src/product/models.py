from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Product(models.Model):
    """
    Represents product object
    """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    """
    Category can be modified to independent model.
    """
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Represents user opinion on product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()

    def __str__(self):
        return f'{self.author} rating {self.rate} on {self.product} '
