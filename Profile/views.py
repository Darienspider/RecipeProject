from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required 
def profile(request,user_id):
    profile_user = User.objects.all().filter(id = user_id)
     