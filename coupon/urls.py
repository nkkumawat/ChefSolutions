from django.contrib import admin
from django.urls import path, include
from .views import checkCoupon , removeCoupon
app_name = 'coupon'

urlpatterns = [
    path('check', checkCoupon, name="checkCoupon"),
    path('remove', removeCoupon, name="removeCoupon"),
]
