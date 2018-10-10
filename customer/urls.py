from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import login, signup, dashboard, logout


urlpatterns = [
    path('login',login , name="login"),
    path('logout',logout, name="logout"),
    path('signup',signup, name="signup"),
    path('dashboard',dashboard, name="dashboard"),
]