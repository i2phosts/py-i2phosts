import re

from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from web.postkey.models import i2phost
from web.lib.validation import validate_hostname
from web import settings

def jumper(request, host):
	"""Actually do jumps."""
	try:
		hostname = validate_hostname(host)
	except ValidationError, e:
		return redirect('/jump/error/')
	try:
		key = i2phost.objects.get(name=hostname, activated=True).b64hash
	except i2phost.DoesNotExist:
		return redirect('/jump/unknown/')
	url = 'http://' + hostname + '/?i2paddresshelper=' + key
	# get params from requst string, e.g. from 'example.i2p/smth/1?a=b&c=d' get 'smth/1?a=b&c=d'
	pattern = host + r'/(.+)'
	m = re.search(pattern, request.get_full_path())
	if m:
		params = m.group(1)
		url += '/' + params
	return render_to_response('jump.html', {
		'title': settings.SITE_NAME,
		'url': url,
		})

def error(request):
	return HttpResponse('You are trying to access an invalid hostname.')

def unknown(request):
	return HttpResponse('You are trying to access an unknown hostname.')
