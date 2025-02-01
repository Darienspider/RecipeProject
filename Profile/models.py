from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Recipe/recipe_images', default=f'{str(user).replace(' ','_')}default.jpg')
    bio = models.TextField(max_length=1024)

    def __str__(self):
        return self.user.username
