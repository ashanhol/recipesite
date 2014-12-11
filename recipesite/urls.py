from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^addrecipe/', include('addrecipe.urls', namespace="addrecipe")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^home/', include('home.urls', namespace="home")),
    url(r'^menu/', include('menu.urls', namespace="menu")),
    url(r'^admin/', include(admin.site.urls)),
]
