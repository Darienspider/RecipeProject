"""
URL configuration for RecipeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import projectHome, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view = projectHome, name = 'projectHome'),
    path('Blog/', include('Blog.urls'), name="BlogMain"),
    path('Recipe/', include('Recipe.urls'), name = "recipeMain"),
    path('Inventory/', include('Inventory.urls'), name = "inventoryMain"),
    path('Profile/', include('Profile.urls'), name = "profileMain"),
    path("Login/" , name='login', view=login_view),  # handles logins, logouts, etc
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
