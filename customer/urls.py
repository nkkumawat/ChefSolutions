from django.contrib import admin
from django.urls import path , re_path
from django.conf.urls import url
from .views import login, signup, dashboard, logout, forgotPassword, changePassword, accoutVarification


urlpatterns = [
    path('login',login , name="login"),
    path('logout',logout, name="logout"),
    path('signup',signup, name="signup"),
    re_path(r'^forgotpassword',forgotPassword, name="forgot"),
    re_path(r'^varify',accoutVarification, name="varify"),
    path('changepassword',changePassword, name="changepassword"),
    path('dashboard',dashboard, name="dashboard"),
]