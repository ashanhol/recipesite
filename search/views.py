#!/usr/bin/python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from django.db.models import Q
from addrecipe.models import Recipe, Ingredient, Instruction
from search.forms import searchForm



def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    #Splits the query string in invidual keywords, getting rid of unecessary spaces and grouping quoted words together.
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 



def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        searchform = searchForm(request.POST)
        
        # check whether it's valid:
        if searchform.is_valid():
            
            searchquery = searchform.save(commit=False)
            
            #search different terms by separating with ',' 
            searchterm = searchquery.cleaned_data['search_box'].split(',')
            or_query = None
            for term in searchterm:
                
                q = Q(recipe_name__icontains=term)
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            
            results = Recipe.objects.all().filter(or_query)

            
            searchquery.save()
            
            # redirect to a new URL:
            ##########
            return HttpResponseRedirect(reverse('addrecipe:thank', args=(savedrecipe.id,)))
            
    # if a GET (or any other method) we'll create a blank form
    else:
        searchform = searchForm()

    ##########
    return render(request, 'search/index.html', {'searchform': searchform})
