from django.contrib import admin
from django.urls import path, include
from .views import addRecipe, recipes, printRecipe

app_name = 'blog'

urlpatterns = [
    path('add', addRecipe, name="addrecipe"),
    path('print_recipe/<int:rid>', printRecipe, name="printrecipe"),
    path('', recipes, name="recipe"),
]
