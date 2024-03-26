from django.db import models


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
