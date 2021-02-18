from django.urls import path

from order import views

urlpatterns = [
    path('', views.index, name='index'),
]
