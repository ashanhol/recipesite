from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from addrecipe.models import Recipe
from django.forms.formsets import formset_factory, BaseFormSet
from addrecipe.forms import AddRecipeForm, AddIngredientForm, AddInstructionForm

# Create your views here.
   

def thank_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/addrecipe/')
    return render(request, 'addrecipe/thank.html')



def add_recipe(request):
    # if this is a POST request we need to process the form data
    ingredientformset = formset_factory(AddIngredientForm, extra = 3, can_delete = True)
    instructionformset = formset_factory(AddInstructionForm, extra = 2, can_delete = True)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        recipeform = AddRecipeForm(request.POST)
        ingrformset = ingredientformset(request.POST, request.FILES, prefix = 'ingredients')
        instrucformset = instructionformset(request.POST, request.FILES, prefix = 'instructions')
        #ingredientform = AddIngredientForm(request.POST)
        #instructionform = AddInstructionForm(request.POST)
        # check whether it's valid:
        if recipeform.is_valid() and ingrformset.is_valid() and instrucformset.is_valid():
            # Prepare the ingredient model, but don't commit it to the database
            # just yet.
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
            
            #instruction = instructionform.save(commit=False)
            
           
            #ingredient.recipe = savedrecipe
            #instruction.recipe = savedrecipe
            
            # Save the main object and continue
            #ingredient.save()
            #instruction.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect('thank/')

    # if a GET (or any other method) we'll create a blank form
    else:
        recipeform = AddRecipeForm()
        #ingredientform = AddIngredientForm()
        ingrformset = ingredientformset(prefix = 'ingredients')
        #instructionform = AddInstructionForm()
        instrucformset = instructionformset(prefix = 'instructions')

    return render(request, 'addrecipe/index.html', {'recipeform': recipeform, 'ingrformset' : ingrformset, 'instrucformset' : instrucformset })

    
