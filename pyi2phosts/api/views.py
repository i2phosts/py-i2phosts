import simplejson as json

from django.http import HttpResponse

from pyi2phosts.postkey.models import i2phost
from pyi2phosts.lib.utils import get_b32

def all(request):
	"""Return all hosts in { "b32": "last seen timestamp" } form. Implemented by zzz request. """
	# all hosts seen at least once
	queryset = i2phost.objects.exclude(last_seen=None)
	json_dict = {}
	for host in queryset:
		# pass last_seen to json in unixtime
		json_dict[get_b32(host.b64hash)] = host.last_seen.strftime("%s")
	return HttpResponse(json.dumps(json_dict), mimetype="application/json")
