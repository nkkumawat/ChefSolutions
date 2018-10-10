
from django.urls import path , re_path
from .views import error
urlpatterns = [
    path('',error , name="login"),

]