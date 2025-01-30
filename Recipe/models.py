from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recipe(models.Model):
    timeframes = [
        ('minutes', str('minutes').upper()),
        ('hours', str('hours').upper()),
        ('days', str('days').upper()),
        ('weeks', str('weeks').upper()),
        ('months', str('months').upper()),
        ('years', str('years').upper())
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Recipe/recipe_images', default=f'{str(title).replace(' ','_')}default.jpg')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    prep_time = models.IntegerField()

    class Meta:
        verbose_name ='Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title
    

    

class Steps(models.Model):
    step = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Step'
        verbose_name_plural = 'Steps'


    def __str__(self):
        return self.step
    
class Ingredients(models.Model):
    ingredient = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self):
        return self.ingredient
    class Meta:
        verbose_name ='Ingredient'
        verbose_name_plural = 'Ingredients'