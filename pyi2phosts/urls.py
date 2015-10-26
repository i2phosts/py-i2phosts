from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

from pyi2phosts.lib.rss import AliveHostsFeed
from pyi2phosts.lib.generic import LocalTemplateView
from pyi2phosts.lib.generic import FaqView
from pyi2phosts.lib.generic import HostsListsView


urlpatterns = patterns('',
        url(r'^$', LocalTemplateView.as_view(template_name='index.html'), name='index'),
        url(r'^contacts/$',  LocalTemplateView.as_view(template_name='contacts.html'), name='contacts'),
        url(r'^faq/$', FaqView.as_view(), name='faq'),
        url(r'^browse/$', HostsListsView.as_view(), name='browse'),
        url(r'^browse/rss/$', AliveHostsFeed(), name='browse-rss'),

        (r'^latest/', include('pyi2phosts.latest.urls')),
        (r'^search/$', include('pyi2phosts.search.urls')),
        (r'^postkey/', include('pyi2phosts.postkey.urls')),
        (r'^jump/', include('pyi2phosts.jump.urls')),
        (r'^api/', include('pyi2phosts.api.urls')),
        (r'^i18n/', include('django.conf.urls.i18n')),
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
