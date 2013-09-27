import datetime

from django.conf import settings

from pyi2phosts.postkey.models import i2phost
from pyi2phosts.lib.generic import HostsListsView

def get_latest():
	now_date = datetime.datetime.utcnow()
	start_date = now_date - datetime.timedelta(days=settings.LATEST_DAY_COUNT)
	qs = i2phost.objects.filter(activated=True,
			date_added__range=(start_date, now_date)).order_by("-date_added")[:settings.LATEST_HOSTS_COUNT]
	return qs

class LatestHostsListsView(HostsListsView):
	""" Renders list of latest active hosts added """

	def get_context_data(self, **kwargs):
		context = super(LatestHostsListsView, self).get_context_data(**kwargs)
		context.update({
			'title': settings.SITE_NAME,
			'day_count': settings.LATEST_DAY_COUNT,
			'hosts_count': settings.LATEST_HOSTS_COUNT
		})
		return context

	queryset = get_latest()
	template_name = 'latest.html'
	template_object_name = 'host_list'
	paginate_by = 40
