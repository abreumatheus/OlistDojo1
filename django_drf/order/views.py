from rest_framework import viewsets
from order.models import Order
from order.serializers import OrderSerializer

def index():
    return 'Bem vindo Order'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
