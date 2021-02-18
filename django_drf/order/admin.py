from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'get_product_name', 'get_seller_name')

    def get_seller_name(self, obj):
        return ', '.join([p.seller.name for p in obj.product.all()])

    def get_product_name(self, obj):
        return ', '.join([p.name for p in obj.product.all()])
