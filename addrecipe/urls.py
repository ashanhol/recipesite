from django.conf.urls import url

from addrecipe import views

urlpatterns = [
    url(r'^(?P<recipe_id>[0-9]+)/thank/$', views.thank_view, name = 'thank'),
    url(r'^$', views.add_recipe, name = 'add_recipe'),
    url(r'^(?P<recipe_id>[0-9]+)/edit/$', views.recipe_edit, name = 'recipe_edit'),


]