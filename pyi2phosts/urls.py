import datetime
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pyi2phosts.lib.utils import get_b32
from pyi2phosts.extsources.models import ExternalSource
from pyi2phosts.postkey.models import i2phost
import settings

extsources = {
		'queryset': ExternalSource.objects.filter(active=True),
		'template_name': 'faq.html',
		'template_object_name': 'sources',
		'extra_context': {
			'title': settings.SITE_NAME,
			}
		}

browse_hosts = {
		'queryset': i2phost.objects.filter(activated=True).order_by("-last_seen"),
		'template_name': 'browse.html',
		'template_object_name': 'host',
		'paginate_by': 40,
		'extra_context': {
			'title': settings.SITE_NAME,
			}
		}

day_count = 30
hosts_count = 40
now_date = datetime.datetime.utcnow()
start_date = now_date - datetime.timedelta(days=day_count)
latest_hosts = {
		'queryset': i2phost.objects.filter(activated=True,
			date_added__range=(start_date, now_date)).order_by("-date_added")[:hosts_count],
		'template_name': 'latest.html',
		'template_object_name': 'host',
		'paginate_by': 40,
		'extra_context': {
			'title': settings.SITE_NAME,
			'day_count': day_count,
			'hosts_count': hosts_count,
			}
		}

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
		url(r'^faq/$', object_list, extsources, name='faq'),
		url(r'^browse/$', object_list, browse_hosts, name='browse'),
		url(r'^latest/$', object_list, latest_hosts, name='latest'),
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
