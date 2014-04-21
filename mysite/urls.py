from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover() #these two lines enable the admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blog/', include('blog.urls')),
    url(r'^latestnews', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', include('blog.urls')),

)
