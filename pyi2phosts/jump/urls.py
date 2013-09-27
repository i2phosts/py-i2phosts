from django.conf.urls import *

urlpatterns = patterns('pyi2phosts.jump.views',
		(r'^([^$/]+)', 'jumper'),
		(r'', 'index'),

)
