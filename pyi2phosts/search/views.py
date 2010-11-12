from django.db.models import Q
from django.views.generic import list_detail

import settings
from pyi2phosts.postkey.models import i2phost


def search(request):
	q = request.GET.get('q', '')
	fil = Q(name__icontains=q)
	qs = i2phost.objects.filter(fil)
	return list_detail.object_list(
			request = request,
			queryset = qs,
			template_name = 'search_results.html',
			template_object_name = 'host',
			paginate_by = 40,
			extra_context = {
				'title': settings.SITE_NAME,
				}
			)
