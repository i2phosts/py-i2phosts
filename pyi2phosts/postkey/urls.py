from django.conf.urls import *

urlpatterns = patterns('pyi2phosts.postkey.views',
        (r'^$', 'addkey'),
        (r'^success/', 'success'),
        (r'^subdomain/', 'subdomain'),
)
