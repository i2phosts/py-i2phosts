import datetime

from django.conf import settings
from django.views.generic.list import ListView

from pyi2phosts.postkey.models import i2phost

def get_latest():
    now_date = datetime.datetime.utcnow()
    start_date = now_date - datetime.timedelta(days=settings.LATEST_DAY_COUNT)
    qs = i2phost.objects.filter(activated=True,
            date_added__range=(start_date, now_date)).order_by("-date_added")[:settings.LATEST_HOSTS_COUNT]
    return qs

class LatestHostsListsView(ListView):
    """ Renders list of latest active hosts added """

    queryset = get_latest()
    template_name = 'latest.html'
    context_object_name = 'host_list'
    paginate_by = 40
