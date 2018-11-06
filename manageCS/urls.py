from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import manageOrders, manageOrderSingle, manageProducts, manageProductSingle, addProduct
from  .views import deleteProduct, manageB2BRequest

app_name = 'manageCS'

urlpatterns = [
    path('orders', manageOrders, name="manageOrders"),
    path('orders/single', manageOrderSingle, name="manageOrderSingle"),
    path('products', manageProducts, name="manageProducts"),
    path('products/single', manageProductSingle, name="manageProductSingle"),
    path('products/add', addProduct, name="addProduct"),
    path('products/delete', deleteProduct, name="deleteProduct"),
    path('requests-b2b', manageB2BRequest, name="manageB2BRequest"),
]
