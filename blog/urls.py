from django.contrib import admin
from django.urls import path, include
from .views import addRecipe, recipes

app_name = 'blog'

urlpatterns = [
    path('add', addRecipe, name="addrecipe"),
    path('', recipes, name="recipe"),
]
