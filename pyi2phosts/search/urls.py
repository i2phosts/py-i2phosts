from django.conf.urls import *
from pyi2phosts.search.views import SearchedHostsListsView

urlpatterns = [
        url(r'^$', SearchedHostsListsView.as_view()),
]
