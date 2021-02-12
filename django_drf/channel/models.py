from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    api_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
