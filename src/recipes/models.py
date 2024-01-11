from django.db import models

# Create your models here.
class Recipes(models.Model):
    #Write the fields here
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='In minutes')
    ingredients = models.CharField(max_length=350, 
                                   help_text='Ingredients must be separated by commas.')
    description = models.TextField()

    def __str__(self):
        return self.name