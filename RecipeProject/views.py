from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def projectHome(request):
    context = {
        'title':'RecipeProjectFolder'
    }
    return render(request, 'RecipeProject/main.html', context = context)


def login_view(request):
    context = {
        'title':'Login'
    }
    return render(request, 'RecipeProject/login.html',context=context)

def logout_view(request):
    context = {
        'title':'Logout'
    }

    return render(request, 'RecipeProject/logout.html')
