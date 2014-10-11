from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from addrecipe.models import Recipe
from addrecipe.forms import AddRecipeForm, AddIngredientForm, AddInstructionForm

# Create your views here.


#  Create a form instance from POST data.
#form = AddRecipeForm(request.POST)

# Save a new Recipe object from the form's data.
#new_recipe = form.save()

# Create a form to edit an existing recipe, but use POST data to populate the form.
#recipe = Recipe.objects.get(pk=1)
#form = AddRecipeForm(request.POST, instance=recipe)
#form.save()

#class IndexView(generic.ListView):
#    model = Recipe
#    template_name = 'addrecipe/index.html'    

def thank_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/addrecipe/')
    return render(request, 'addrecipe/thank.html')



def add_recipe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        recipeform = AddRecipeForm(request.POST)
        ingredientform = AddIngredientForm(request.POST)
        instructionform = AddInstructionForm(request.POST)
        # check whether it's valid:
        if recipeform.is_valid() and ingredientform.is_valid() and instructionform.is_valid():
            # Prepare the ingredient model, but don't commit it to the database
            # just yet.
            ingredient = ingredientform.save(commit=False)
            instruction = instructionform.save(commit=False)
            
            # Add the recipe ForeignKey by saving the secondary form we setup
            savedrecipe= recipeform.save()
            ingredient.recipe = savedrecipe
            instruction.recipe = savedrecipe
            
            # Save the main object and continue
            ingredient.save()
            instruction.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect('thank/')

    # if a GET (or any other method) we'll create a blank form
    else:
        recipeform = AddRecipeForm()
        ingredientform = AddIngredientForm()
        instructionform = AddInstructionForm()

    return render(request, 'addrecipe/index.html', {'recipeform': recipeform, 'ingredientform' : ingredientform, 'instructionform' : instructionform})

    
