#!/usr/bin/python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

import json
from django.http import HttpResponse
from django.core import serializers


from django.db.models import Q
from addrecipe.models import Recipe, Ingredient, Instruction
from search.forms import searchForm


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        searchform = searchForm(request.POST)
        
        # check whether it's valid:
        #if searchform.is_valid():
            
        response_data = {}            
        
            #search different terms by separating with ',' 
        #searchterm = searchform.cleaned_data['search_box'].split(',')
        post_text = request.POST.get('the_post')
        searchterm = post_text.split(',')


        or_query = None
        
        for term in searchterm:
            q = None
            #if request.POST.get('searchtype') == 'NAME':
            q = Q(recipe_name__icontains=term)
            #elif request.POST.get('searchtype') == 'INGR':
            #    q = Q(ingredient_text__icontains=term)

            
            #ORing search terms together 
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
            
            #Get QuerySet based on restrictions and search terms
            #results = None
            #if request.POST.get('searchtype') == 'NAME':
            results = Recipe.objects.all().filter(or_query)
            #elif request.POST.get('searchtype') == 'INGR':
            #    results = Ingredient.objects.all().filter(or_query)


            
            if request.POST.get('vegetarian') == 'true':
                results = results.filter(vegetarian = True)
            if request.POST.get('vegan') == 'true':
                results = results.filter(vegan = True)
            if request.POST.get('glutenfree') == 'true':
                results = results.filter(gluten_free = True)
            if request.POST.get('soyfree') == 'true':
                results = results.filter(soy_free = True)
            if request.POST.get('dairyfree') == 'true':
                results = results.filter(dairy_free = True)
            
            
            #separate each recipe into its components to pass into JSON
            individual_recipes = [result.recipe_name for result in results]
            ingredients = []
            instructions = []
            for result in results:
                ings = result.ingredient_set.all()
                individ_ing =[]
                for ing in ings:
                    individ_ing.append(ing.ingredient_text)
                ingredients.append(individ_ing)
                
                
                insts = result.instruction_set.all()
                individ_inst = []
                for inst in insts:
                    individ_inst.append(inst.instruction_text)
                instructions.append(individ_inst)
                    
                    
            #ingredients = serializers.serialize("json", ingredients)
            #instructions = serializers.serialize("json", instructions)

            response_data['recipe_names'] = individual_recipes
            response_data['recipe_ing'] = ingredients
            response_data['recipe_inst'] = instructions
            
            # redirect to a new URL:
            ##########
            #return HttpResponseRedirect(reverse('addrecipe:thank', args=(savedrecipe.id,)))
            return HttpResponse(json.dumps(response_data), content_type="application/json")   

    # if a GET (or any other method) we'll create a blank form
    else:
        searchform = searchForm()

    ##########
    return render(request, 'search/index.html', {'searchform': searchform})
