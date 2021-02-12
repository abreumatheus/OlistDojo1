from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=11, null=False)
    num_doc = models.CharField(max_length=15, null=False)

    def __str__(self):
        return f'{self.name} {self.phone} {self.num_doc}'
