from django.shortcuts import render

# Create your views here.


def error(request):
    return render(request, "error.html")