from django.contrib import admin
from .models import Product, Category
from seller.models import Seller


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'create_at', 'update_at', 'get_category_name', 'get_seller_name')

    def get_seller_name(self, obj):
        return obj.seller.name

    def get_category_name(self, obj):
        return ", ".join([e.name for e in obj.category.all()])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')





