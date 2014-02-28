from django.conf.urls import patterns, include, url
from my_site.views import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^blog/', include('blog.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
