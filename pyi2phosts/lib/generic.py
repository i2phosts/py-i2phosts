from django.views.generic.base import TemplateView
from pyi2phosts.lib.utils import get_b32
import settings

class LocalTemplateView(TemplateView):
	def get_context_data(self, **kwargs):
	        context = super(LocalTemplateView, self).get_context_data(**kwargs)
	        context.update({
			'title': settings.SITE_NAME,
			'domain': settings.DOMAIN,
			'b64': settings.MY_B64,
			'b32': get_b32(settings.MY_B64)
		})
		return context
