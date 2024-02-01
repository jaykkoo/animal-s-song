from django.shortcuts import render
from django.views.generic import ListView
from .models import Animal

def home(request):
    animals = Animal.objects.all()[:3]
    context = {
        'animals': animals
        }
    return render(request, 'home.html', context)

class ListAnimal(ListView):
    model = Animal
    template_name = 'list.html'
    context_object_name = 'animals'
    ordering = ['-id']  # Order the items by their ID in descending order
        