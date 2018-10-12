
from django.contrib import admin
from django.urls import path , include, re_path
from .views import allProducts, prductDetail

urlpatterns = [
    path('',allProducts , name="all products"),
    path('details/<int:pid>' , prductDetail , name="product details"),

]