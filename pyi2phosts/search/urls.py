from django.conf.urls.defaults import *
from pyi2phosts.search.views import SearchedHostsListsView

urlpatterns = patterns('',
		(r'^$', SearchedHostsListsView.as_view()),
)
