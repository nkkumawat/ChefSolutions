
from django.contrib import admin
from django.urls import path, include, re_path
from .views import allProducts, prductDetail

app_name = 'products'

urlpatterns = [
    path('', allProducts, name="all_products"),
    path('details/<int:pid>', prductDetail, name="product details"),
]
