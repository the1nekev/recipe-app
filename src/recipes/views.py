from django.shortcuts import render
from django.views.generic import ListView, DetailView #to display lists and details
from .models import Recipes #to access Recipes Model

# used to protect class-based view (require authentication to display in browser)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def welcome(request):
    return render(request, 'recipes/recipes_home.html')

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'
