from django.contrib import admin
from django.urls import path, include
from .views import addRecipe, recipes, printRecipe, recipesDetail

app_name = 'blog'

urlpatterns = [
    path('', recipes, name="recipe"),
    path('<int:id>/', recipesDetail, name="recipesDetail"),
    path('add', addRecipe, name="addrecipe"),
    path('print_recipe/<int:rid>', printRecipe, name="printrecipe"),
]
