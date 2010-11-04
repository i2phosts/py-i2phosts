from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pyi2phosts.other.views import *

urlpatterns = patterns('',
		url(r'^$', index, name='index'),
		(r'^postkey/', include('pyi2phosts.postkey.urls')),
		(r'^jump/', include('pyi2phosts.jump.urls')),
    # Example:
    # (r'^pyi2phosts.', include('pyi2phosts.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
