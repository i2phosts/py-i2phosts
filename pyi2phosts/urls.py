from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

from pyi2phosts.lib.rss import AliveHostsFeed
from pyi2phosts.lib.generic import FaqView
from pyi2phosts.lib.generic import HostsListsView
from pyi2phosts.pages.views import PageView


urlpatterns = [
        url(r'^faq/$', FaqView.as_view(), name='faq'),
        url(r'^subscription/$', TemplateView.as_view(template_name='subscription.html'), name='subscription'),
        url(r'^browse/$', HostsListsView.as_view(), name='browse'),
        url(r'^browse/rss/$', AliveHostsFeed(), name='browse-rss'),

        url(r'^latest/', include('pyi2phosts.latest.urls')),
        url(r'^search/', include('pyi2phosts.search.urls')),
        url(r'^postkey/', include('pyi2phosts.postkey.urls')),
        url(r'^jump/', include('pyi2phosts.jump.urls')),
        url(r'^api/', include('pyi2phosts.api.urls')),
        url(r'^i18n/', include('django.conf.urls.i18n')),

        # put your custom pages here
        url(r'^$', PageView.as_view(), {'page_name': 'index'}, name='index'),
        url(r'^(?P<page_name>contacts)/$', PageView.as_view(), name='page'),

        # admin site
        url(r'^admin/', admin.site.urls),
]
