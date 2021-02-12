from django.db import models
from product.models import Product


class Order(models.Model):
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
