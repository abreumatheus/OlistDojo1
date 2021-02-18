from django.urls import path
from seller import views

urlpatterns = [
    path('', views.index, name='index'),
]