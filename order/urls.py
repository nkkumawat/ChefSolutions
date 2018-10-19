from django.contrib import admin
from django.urls import path, re_path
from .views import placeOrder


urlpatterns = [
    path('', placeOrder, name="placeorder"),
]
