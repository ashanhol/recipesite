from django.conf.urls import url

from menu import views

urlpatterns = [
    
    url(r'^$', views.get_menu, name = 'get_menu'),
    url(r'^(?P<recipe_id>[0-9]+)/yourmenu/$', views.add_menu, name = 'add_menu'),
    url(r'^(?P<recipe_id>[0-9]+)/updatedmenu/$', views.remove_from_menu, name = 'rem_menu'),

]