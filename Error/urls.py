from django.urls import path, re_path
from .views import error

app_name = 'error'

urlpatterns = [
    path('', error, name="error"),
]
