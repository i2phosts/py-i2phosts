from django.conf.urls.defaults import *
from pyi2phosts.lib.rss import LatestHostsFeed

urlpatterns = patterns('pyi2phosts.latest.views',
		url(r'^$', 'latest', name='latest'),
		url(r'^rss/$', LatestHostsFeed()),

)
