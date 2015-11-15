from django.db.models import Q

from pyi2phosts.postkey.models import i2phost
from pyi2phosts.lib.generic import LocalObjectList


class SearchedHostsListsView(LocalObjectList):
    """ Renders list of hosts matching search request """

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        fil = Q(name__icontains=q) | Q(b64hash__contains=q)
        queryset = i2phost.objects.filter(fil)
        return queryset

    template_name = 'search_results.html'
    context_object_name = 'host_list'
    paginate_by = 40
