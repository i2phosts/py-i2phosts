from django.conf.urls.defaults import *

urlpatterns = patterns('pyi2phosts.postkey.views',
		(r'^$', 'addkey'),
		(r'^success/', 'success'),
)
