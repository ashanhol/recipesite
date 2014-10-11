from django.contrib import admin
from addrecipe.models import Recipe, Ingredient, Instruction

# Register your models here.

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 4

class InstructionInline(admin.StackedInline):
    model = Instruction
    extra = 4

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline]
    search_fields = ['recipe_name']




admin.site.register(Recipe, RecipeAdmin)
