from django.shortcuts import render_to_response

from pyi2phosts.lib.utils import get_b32

import settings

def index(request):
	return render_to_response('index.html', {
		'title': settings.SITE_NAME,
		'domain': settings.DOMAIN,
		'b64': settings.MY_B64,
		'b32': get_b32(settings.MY_B64),
		})
