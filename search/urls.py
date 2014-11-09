from django.conf.urls import url

from search import views

urlpatterns = [
    
    url(r'^$', views.add_recipe, name = 'add_recipe'),

]