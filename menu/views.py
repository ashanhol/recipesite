from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse

from addrecipe.models import Recipe, Ingredient, Instruction
from menu.create_menu import Menus


def add_menu(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    menu = Menus(request)
    menu.add(recipe)
    return HttpResponseRedirect(reverse('menu:get_menu'))
#    return render_to_response('menu/menu.html', dict(menu=Menus(request)))


def remove_from_menu(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    menu = Menus(request)
    menu.remove(recipe)
    return render_to_response('menu/menu.html', dict(menu=Menus(request)))


def get_menu(request):
    return render_to_response('menu/menu.html', dict(menu=Menus(request)))


