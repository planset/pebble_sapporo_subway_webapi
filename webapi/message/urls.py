from django.conf.urls import patterns

urlpatterns = patterns('message.views',
    (r'^[/]?$', 'list_message'),
    (r'^add$', 'add_message'),
)

