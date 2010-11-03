from django.conf.urls.defaults import *

urlpatterns = patterns('jump.views',
		(r'^([^$/]+)', 'jumper'),

)
