from django.conf.urls import patterns, include, url

urlpatterns = patterns('videopbi.views',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)$', 'show'),
    (r'^upload/(?P<id>\d+)$', 'upload'),
    (r'^(?P<id>\d+)/start$', 'start'),
    (r'^(?P<id>\d+)/stop$', 'stop'),
)
