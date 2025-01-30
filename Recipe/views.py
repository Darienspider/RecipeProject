from django.shortcuts import render
from .models import Recipe, Steps, Ingredients

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    context = {
        'title': 'Recipe App',
        'recipes': recipes,
    }
    return render(request, 'Recipe/RecipeMain.html', context)

def details(request, id):
    context = {
        'title':'Recipe Details',
        'Recipe':Recipe.objects.get(id=id) ,
        'Steps': Steps.objects.filter(recipe=id),
    }

    return render(request, 'Recipe/RecipeDetails.html', context = context)