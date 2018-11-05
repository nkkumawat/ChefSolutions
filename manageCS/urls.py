from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import manageOrders, manageOrderSingle

app_name = 'manageCS'

urlpatterns = [
    path('orders', manageOrders, name="manage"),
    path('orders/single', manageOrderSingle, name="manage"),
]
