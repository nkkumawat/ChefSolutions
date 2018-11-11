from django.shortcuts import render
import getResponses


def homepage(request):
    data = getResponses.getResponse(request)
    return render(request, 'base/index.html', data)


def aboutus(request):
    return render(request, 'base/aboutus.html')
