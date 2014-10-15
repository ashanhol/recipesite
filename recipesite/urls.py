from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^addrecipe/', include('addrecipe.urls', namespace="addrecipe")),
    
    url(r'^admin/', include(admin.site.urls)),
]
