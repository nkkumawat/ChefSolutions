from django.contrib import admin
from django.urls import path , include
from .views import addRecipe, recipes


urlpatterns = [
    path('/add' , addRecipe , name="add reecipe"),
    path('' , recipes , name="reecipe"),

]
