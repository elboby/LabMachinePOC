from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('labmachine.apps.branch.views',
    url(r'^$', 'list', name="branch-list"),
    url(r'^list/$', 'list', name="branch-list"),
    
    url(r'^(\d)$', 'view', name="branch-view"),
    
    url(r'^create/(\d)$', 'create', name="branch-create"),
)