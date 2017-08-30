from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

from django.conf import settings

from pyi2phosts.lib.rss import AliveHostsFeed
from pyi2phosts.lib.generic import LocalTemplateView
from pyi2phosts.lib.generic import FaqView
from pyi2phosts.lib.generic import HostsListsView


urlpatterns = [
        url(r'^$', LocalTemplateView.as_view(template_name='index.html'), name='index'),
        url(r'^contacts/$',  LocalTemplateView.as_view(template_name='contacts.html'), name='contacts'),
        url(r'^faq/$', FaqView.as_view(), name='faq'),
        url(r'^browse/$', HostsListsView.as_view(), name='browse'),
        url(r'^browse/rss/$', AliveHostsFeed(), name='browse-rss'),

        url(r'^latest/', include('pyi2phosts.latest.urls')),
        url(r'^search/', include('pyi2phosts.search.urls')),
        url(r'^postkey/', include('pyi2phosts.postkey.urls')),
        url(r'^jump/', include('pyi2phosts.jump.urls')),
        url(r'^api/', include('pyi2phosts.api.urls')),
        url(r'^i18n/', include('django.conf.urls.i18n')),

        # admin site
        url(r'^admin/', admin.site.urls),
]
