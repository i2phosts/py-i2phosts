from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from web.postkey.models import i2phost
from web.lib.validation import validate_hostname

def jumper(request, data):
	"""Actually do jumps."""
	try:
		hostname = validate_hostname(data)
	except ValidationError, e:
		return redirect('/jump/error/')
	try:
		key = i2phost.objects.get(name=hostname, activated=True).b64hash
	except i2phost.DoesNotExist:
		return redirect('/jump/unknown/')
	url = 'http://' + hostname + '/?i2paddresshelper=' + key
	return redirect(url, permanent=True)

def error(request):
	return HttpResponse('You are trying to access an invalid hostname.')

def unknown(request):
	return HttpResponse('You are trying to access an unknown hostname.')
