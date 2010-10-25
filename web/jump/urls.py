from django.conf.urls.defaults import *

urlpatterns = patterns('web.jump.views',
		(r'^([^$/]+)', 'jumper'),

)
