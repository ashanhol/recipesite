#!/usr/bin/python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from addrecipe.models import Recipe, Ingredient, Instruction
from django.forms.formsets import formset_factory, BaseFormSet
from addrecipe.forms import AddRecipeForm, AddIngredientForm, AddInstructionForm

# Create your views here.
   

def thank_view(request, recipe_id):
    if request.method == 'POST':
        return HttpResponseRedirect('/addrecipe/')
    
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'addrecipe/thank.html', {'recipe': recipe})


def add_recipe(request):
    # if this is a POST request we need to process the form data
    ingredientformset = formset_factory(AddIngredientForm, can_delete = True)
    instructionformset = formset_factory(AddInstructionForm, can_delete = True)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        recipeform = AddRecipeForm(request.POST)
        ingrformset = ingredientformset(request.POST, request.FILES, prefix = 'ingredients')
        instrucformset = instructionformset(request.POST, request.FILES, prefix = 'instructions')

        # check whether it's valid:
        if recipeform.is_valid() and ingrformset.is_valid() and instrucformset.is_valid():
            # Prepare the ingredient and instruction models, but don't commit it to the database just yet.
            # Add the recipe ForeignKey by saving the secondary form we setup
            savedrecipe = recipeform.save()
            
            for ingrform in ingrformset:
                ingredient = ingrform.save(commit=False)
                ingredient.recipe = savedrecipe
                ingredient.save()
            
            for instrucform in instrucformset:
                instruction = instrucform.save(commit = False)
                instruction.recipe = savedrecipe
                instruction.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('addrecipe:thank', args=(savedrecipe.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        recipeform = AddRecipeForm()
        ingrformset = ingredientformset(prefix = 'ingredients')
        instrucformset = instructionformset(prefix = 'instructions')

    return render(request, 'addrecipe/index.html', {'recipeform': recipeform, 'ingrformset' : ingrformset, 'instrucformset' : instrucformset })

def recipe_edit(request, recipe_id):
    
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    for ingredient in recipe.ingredient_set.all():
        get_object_or_404(Ingredient, pk=ingredient.id)
    for instruction in recipe.instruction_set.all():
        get_object_or_404(Instruction, pk=instruction.id)
    
     # if this is a POST request we need to process the form data
    ingredientformset = formset_factory(AddIngredientForm, can_delete = True, extra = 0)
    instructionformset = formset_factory(AddInstructionForm, can_delete = True, extra = 0)
    extraingredientformset = formset_factory(AddIngredientForm, can_delete = True)
    extrainstructionformset = formset_factory(AddInstructionForm, can_delete = True)


    
    if request.method == "POST":
        recipeform = AddRecipeForm(request.POST, instance=recipe)
        ingrformset = ingredientformset(request.POST, request.FILES, prefix = 'ingredients', initial=recipe.ingredient_set.all().values())
        instrucformset = instructionformset(request.POST, request.FILES, prefix = 'instructions', initial=recipe.instruction_set.all().values())
        extraingrformset = extraingredientformset(request.POST, request.FILES, prefix = 'extra_ingredients')
        extrainstrucformset = extrainstructionformset(request.POST, request.FILES, prefix = 'extra_instructions')
        
        if recipeform.is_valid() and ingrformset.is_valid() and instrucformset.is_valid() and extraingrformset.is_valid() and extrainstrucformset.is_valid():
            # Prepare the ingredient and instruction models, but don't commit it to the database just yet.
            # Add the recipe ForeignKey by saving the secondary form we setup
            savedrecipe = recipeform.save()
            
            for ingrform in ingrformset:
                ingredient = ingrform.save(commit=False)
                ingredient.recipe = savedrecipe
                ingredient.save()
            
            for ingrform in extraingrformset:
                ingredient = ingrform.save(commit=False)
                ingredient.recipe = savedrecipe
                ingredient.save()
            
            for instrucform in instrucformset:
                instruction = instrucform.save(commit = False)
                instruction.recipe = savedrecipe
                instruction.save()
                
            for instrucform in extrainstrucformset:
                instruction = instrucform.save(commit = False)
                instruction.recipe = savedrecipe
                instruction.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('addrecipe:thank', args=(savedrecipe.id,)))
        
    else:
        recipeform = AddRecipeForm(instance=recipe)
        ingrformset = ingredientformset(prefix = 'ingredients', initial=recipe.ingredient_set.all().values())
        instrucformset = instructionformset(prefix = 'instructions', initial=recipe.instruction_set.all().values())
        extraingrformset = extraingredientformset(prefix = 'extra_ingredients')
        extrainstrucformset = extrainstructionformset(prefix = 'extra_instructions')
        
    return render(request, 'addrecipe/post_edit.html', {'recipeform': recipeform, 'ingrformset' : ingrformset, 'instrucformset' : instrucformset , 'extra_ingredients' : extraingrformset, 'extra_instructions' : extrainstrucformset, 'recipe' : recipe})    
