from django.shortcuts import render
from .models import Recipe, Steps, Ingredients
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.'

def home(request):
    recipes = Recipe.objects.all()
    context = {
        'title': 'Recipe App',
        'recipes': recipes,
        'app_name': 'Recipe',
        'logged_in':request.user.id,
    }
    return render(request, 'Recipe/RecipeMain.html', context)

def details(request, id):
    context = {
        'title':'Recipe Details',
        'Recipe':Recipe.objects.get(id=id) ,
        'Steps': Steps.objects.filter(recipe=id),
    }

    return render(request, 'Recipe/RecipeDetails.html', context = context)