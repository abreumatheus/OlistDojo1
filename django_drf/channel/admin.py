from django.contrib import admin
from channel.models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'created_at')
