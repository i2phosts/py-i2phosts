import re

from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError

from web.postkey.models import i2phost
from web.lib.validation import validate_hostname
from web import settings

def jumper(request, host):
	"""Actually do jumps."""
	try:
		hostname = validate_hostname(host)
	except ValidationError, e:
		return render_to_response('jump-error.html', {
			'title': settings.SITE_NAME,
			'error': e,
			})
	try:
		key = i2phost.objects.get(name=hostname, activated=True).b64hash
	except i2phost.DoesNotExist:
		return render_to_response('jump-unknown.html', {
			'title': settings.SITE_NAME,
			})
	# begin forming url
	url = 'http://' + hostname
	# get params from requst string, e.g. from 'example.i2p/smth/1?a=b&c=d' get 'smth/1?a=b&c=d'
	pattern = host + r'/(.+)'
	m = re.search(pattern, request.get_full_path())
	if m:
		params = m.group(1)
		url += '/' + params
		# determine how we should pass i2paddresshelper
		# http://zzz.i2p/oldnews.html#jump
		if params.find('?') == -1:
			suffix = '?'
		else:
			suffix = '&'
		url += suffix + 'i2paddresshelper=' + key
	else:
		url += '/?i2paddresshelper=' + key
	return render_to_response('jump.html', {
		'title': settings.SITE_NAME,
		'url': url,
		})
