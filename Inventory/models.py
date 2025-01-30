from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='inventory_images', default=f'{str(name).replace(' ','_')}default.jpg')

    def __str__(self):
        return self.name
    

class InventoryItems(models.Model):
    item = models.CharField(max_length=100)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    count = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Inventory Items'
    def __str__(self):
        return self
    
