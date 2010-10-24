from django.conf.urls.defaults import *

urlpatterns = patterns('web.jump.views',
		(r'^error/', 'error'),
		(r'^unknown/', 'unknown'),
		(r'^([^$/]+)', 'jumper'),

)
