from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pyi2phosts.lib.utils import get_b32
from pyi2phosts.extsources.models import ExternalSource
import settings

urlpatterns = patterns('',
		url(r'^$', direct_to_template, {
			'template': 'index.html',
			'extra_context': {
				'title': settings.SITE_NAME,
				'domain': settings.DOMAIN,
				'b64': settings.MY_B64,
				'b32': get_b32(settings.MY_B64)
				}
			}, name='index'),
		url(r'^faq/$', direct_to_template, {
			'template': 'faq.html',
			'extra_context': {
				'title': settings.SITE_NAME,
				'sources': ExternalSource.objects.filter(active=True)
				}
			}, name='faq'),
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

if settings.DEBUG:
	urlpatterns += patterns('', (r'static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}))
