from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'create_at', 'update_at')


admin.site.register(Product, ProductAdmin)
