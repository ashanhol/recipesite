from django.db import models
from django.forms import ModelForm


UNITS = (
    ('TSP', 'tsp'),
    ('TBSP', 'tbsp'),
    ('CUP', 'cup'),
    ('QT', 'quart'),
    ('PT', 'pint'),
    ('L', 'liters'),
    ('GALLON', 'gallon'),
    ('G', 'grams'),
    ('LBS', 'lbs'),
    ('MLS', 'mLs'),
    ('OBJECT', "of these"),
)


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient_text = models.CharField(max_length=100)
    amount =  models.FloatField(default = 999.9)
    unit = models.CharField(max_length=10, choices=UNITS)  #cups/quarts/tbsp etc. still need to decide about objects
    def __str__(self):
        return self.ingredient_text

   
class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    instruction_text = models.CharField(max_length=200)
#    instruction_number = models.IntegerField(default=1)
    def __str__(self):
        return self.instruction_text



    