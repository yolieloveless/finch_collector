from django.shortcuts import render
from django.http import HttpResponse

class Bird:
    def __init__(self, name, species, description, location):
        self.name = name
        self.species = species
        self.description = description
        self.location = location

birds = [
    Bird('American goldfinch', 'Spinus tristis', 'The American goldfinch is a small finch.', 'North America'),
]

# Create your views here.
def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', { 'birds': birds })
