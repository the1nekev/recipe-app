from django.shortcuts import render
from django.views.generic import ListView, DetailView #to display lists and details
from .models import Recipes #to access Recipes Model

# Create your views here.
def welcome(request):
    return render(request, 'recipes/recipes_home.html')

class RecipesListView(ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'