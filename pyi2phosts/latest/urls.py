from django.conf.urls import *
from pyi2phosts.lib.rss import LatestHostsFeed
from pyi2phosts.latest.views import LatestHostsListsView

urlpatterns = patterns('',
        url(r'^$', LatestHostsListsView.as_view(), name='latest'),
        url(r'^rss/$', LatestHostsFeed(), name='latest-rss'),

)
