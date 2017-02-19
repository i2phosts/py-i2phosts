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
    return HttpResponse(json.dumps(json_dict), content_type="application/json")

def status(request):
    """
        Return all hosts in {
                             "hostname": hostname,
                             "b64": b64,
                             "b32": b32,
                             "last-seen": timestamp
                            } form.
        Implemented by MXPLRS|Kirill request.
    """
    # host status
    if 'q' in request.GET and request.GET['q'] is not None and request.GET['q'] != '':
        hostname = request.GET['q']
    else:
        json_dict = {
                    'error': 'Bad request',
        }
        return HttpResponse(json.dumps(json_dict), content_type="application/json")

    try:
        host = i2phost.objects.get(name=hostname)
    except:
        host = None

    if host and host.last_seen:
        json_dict = {
                    'hostname': host.name,
                    'b64': host.b64hash,
                    'b32': get_b32(host.b64hash),
                    'last-seen': host.last_seen.strftime("%s"),
        }
    elif host and not host.last_seen:
        json_dict = {
                    'hostname': host.name,
                    'b64': host.b64hash,
                    'b32': get_b32(host.b64hash),
                    'error': 'Never seen',
        }
    else:
        json_dict = {
                    'hostname': hostname,
                    'error': 'Not found',
        }

    return HttpResponse(json.dumps(json_dict), content_type="application/json")
