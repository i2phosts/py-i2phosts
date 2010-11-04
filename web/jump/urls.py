from django.conf.urls.defaults import *

urlpatterns = patterns('pyi2phosts.jump.views',
		(r'^([^$/]+)', 'jumper'),

)
