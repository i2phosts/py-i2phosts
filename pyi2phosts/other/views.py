from django.shortcuts import render_to_response
import settings

def index(request):
	return render_to_response('index.html', {
		'title': settings.SITE_NAME,
		'domain': settings.DOMAIN,
		})
