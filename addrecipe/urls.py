from django.conf.urls import url

from addrecipe import views

urlpatterns = [
    url(r'^thank/$', views.thank_view, name = 'thank'),
    url(r'^$', views.add_recipe, name = 'add_recipe'),

]