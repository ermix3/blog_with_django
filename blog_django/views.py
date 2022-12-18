from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'title': "Home"})


def about(request):
    return render(request, 'about.html', {'title': "About Us"})


def contact(request):
    return render(request, 'contact.html', {'title': "Contact Us"})


def notFound(request, exception):
    return render(request, '_404.html', {'title': "404 Not Found"})

