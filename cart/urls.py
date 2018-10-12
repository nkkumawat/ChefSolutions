from django.contrib import admin
from django.urls import path , include
from .views import cart, addInCart, deleteCart

urlpatterns = [
    path('' , cart , name="cart"),
    path('add' , addInCart , name="add cart"),
    path('delete' , deleteCart , name="add cart"),
]
