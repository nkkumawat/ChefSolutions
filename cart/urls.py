from django.contrib import admin
from django.urls import path , include
from .views import cart, addInCart

urlpatterns = [
    path('' , cart , name="cart"),
    path('add' , addInCart , name="add cart"),
]
