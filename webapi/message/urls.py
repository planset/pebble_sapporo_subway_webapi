from django.conf.urls import patterns

urlpatterns = patterns('pebblemessenger.views',
    (r'^messages[/]?$', 'list_message'),
    (r'^messages/add$', 'add_message'),
)

