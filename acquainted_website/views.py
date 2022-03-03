#this is where your requests will be returned with html templates. DONT MIX UP WITH URLS>PY
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def resources(request):
    return render(request, 'resources.html')

def about(request):
    return render(request, 'about.html')

def me(request):
    return render(request, 'me.html')

