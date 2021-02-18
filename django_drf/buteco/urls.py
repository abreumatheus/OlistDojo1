from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('channel/', include('channel.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('seller/', include('seller.urls')),
]
