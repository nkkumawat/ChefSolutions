from django.contrib import admin
from django.urls import path, include
from .views import cart, addInCart, deleteCart, clearCart

app_name = 'cart'

urlpatterns = [
    path('', cart, name="cart"),
    path('add', addInCart, name="addcart"),
    path('delete', deleteCart, name="deletecart"),
    path('clear', clearCart, name="deletecart"),
]
