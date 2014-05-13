from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^stations/', include('station.urls')),
    url(r'^messages/', include('message.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
