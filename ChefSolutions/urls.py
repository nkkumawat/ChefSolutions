"""ChefSolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import homepage, aboutus


urlpatterns = [
    path('', homepage, name="index"),
    path('aboutus', aboutus, name="aboutus"),
    path('auth/', include('social_django.urls', namespace='social')),
    path('customer/', include('customer.urls')),
    path('admin/', admin.site.urls),
    path('error/', include('Error.urls')),
    path('cart/', include('cart.urls')),
    path('products/', include('products.urls')),
    path('placeorder/', include('order.urls')),
    path('blog/', include('blog.urls')),
    path('payment/', include('payment.urls'), name="payment"),
    path('managecs/', include('manageCS.urls'), name="manageCS"),
    path('coupon/', include('coupon.urls'), name="manageCS"),
]
