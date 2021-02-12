from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ChannelSerializer
from .models import Channel


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.AllowAny]
