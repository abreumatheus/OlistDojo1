from django.http import HttpResponse
from rest_framework import viewsets, permissions

from .models import Channel
from .serializers import ChannelSerializer


def index(request):
    return HttpResponse('Bem vindo Channel')


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.AllowAny]
