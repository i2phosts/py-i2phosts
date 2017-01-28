from django.conf.urls import *

urlpatterns = patterns('pyi2phosts.api.views',
        url(r'^all/$', 'all'),
        url(r'^status/$', 'status'),
)
