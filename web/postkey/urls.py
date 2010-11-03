from django.conf.urls.defaults import *

urlpatterns = patterns('postkey.views',
		(r'^$', 'addkey'),
		(r'^success/', 'success'),
)
