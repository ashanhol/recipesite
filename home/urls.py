from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^about/$', views.about_view, name = 'about'),
    url(r'^$', views.home_view, name = 'home_view'),

]