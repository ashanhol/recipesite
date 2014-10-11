from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'recipesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^addrecipe/', include('addrecipe.urls', namespace="addrecipe")),
    
    url(r'^admin/', include(admin.site.urls)),
]
