from django.shortcuts import render

# Create your views here.

def vie(request):
    return render(request, 'page.html')

def home(request):
    return render(request, 'home.html')
        