from django.conf.urls.defaults import *

urlpatterns = patterns('pyi2phosts.latest.views',
		url(r'^$', 'latest', name='latest'),
)
