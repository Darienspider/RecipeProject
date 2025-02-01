from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .settings import personal_apps

def projectHome(request):
    context = {
        'title':'RecipeProjectFolder',
        'apps':[i for i in personal_apps]
    }
    print(context['apps'])
    return render(request, 'RecipeProject/home.html', context = context)


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
