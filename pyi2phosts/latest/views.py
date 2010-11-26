import datetime

from django.views.generic import list_detail

import settings
from pyi2phosts.postkey.models import i2phost

def latest(request):
	now_date = datetime.datetime.utcnow()
	start_date = now_date - datetime.timedelta(days=settings.LATEST_DAY_COUNT)
	qs = i2phost.objects.filter(activated=True,
			date_added__range=(start_date, now_date)).order_by("-date_added")[:settings.LATEST_HOSTS_COUNT]
	return list_detail.object_list(
			request = request,
			queryset = qs,
			template_name = 'latest.html',
			template_object_name = 'host',
			paginate_by = 40,
			extra_context = {
				'title': settings.SITE_NAME,
				'day_count': settings.LATEST_DAY_COUNT,
				'hosts_count': settings.LATEST_HOSTS_COUNT,
				}
			)
