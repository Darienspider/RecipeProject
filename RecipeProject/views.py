from django.shortcuts import render

def projectHome(request):
    context = {
        'title':'RecipeProjectFolder'
    }
    return render(request, 'RecipeProject/main.html', context = context)