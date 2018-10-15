from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import login, signup, profile, logout, forgotPassword, changePassword, accoutVarification
from .views import updatePassword, updateProfile

app_name = 'customer'

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('signup', signup, name="signup"),
    re_path(r'^forgotpassword', forgotPassword, name="forgot"),
    re_path(r'^varify', accoutVarification, name="varify"),
    path('changepassword', changePassword, name="changepassword"),
    path('updatepassword', updatePassword, name="updatepassword"),
    path('updateprofile', updateProfile, name="updateprofile "),
    path('profile', profile, name="profile"),
]
