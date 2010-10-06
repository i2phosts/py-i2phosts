from django.conf.urls.defaults import *

urlpatterns = patterns('web.postkey.views',
		(r'^$', 'addkey'),
		(r'^success/', 'success'),
)
