from django.conf.urls import patterns, include, url

urlpatterns = patterns('station.views',
    (r'^(?P<id>\d+)$', 'show'),
    (r'^(?P<id>\d+)/departures$', 'departures'),
    (r'^closest/(?P<lat>[\d\.]+)/(?P<lng>[\d\.]+)/$', 'closest'),
)
