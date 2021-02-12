from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'
