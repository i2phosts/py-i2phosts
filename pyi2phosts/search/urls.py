from django.conf.urls import *
from pyi2phosts.search.views import SearchedHostsListsView

urlpatterns = patterns('',
		(r'^$', SearchedHostsListsView.as_view()),
)
