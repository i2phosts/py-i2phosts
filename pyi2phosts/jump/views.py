import re
import urllib
import urlparse

from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.template import RequestContext

from pyi2phosts.postkey.models import i2phost
from pyi2phosts.lib.validation import validate_hostname

#https://stackoverflow.com/questions/2778247/how-do-i-construct-a-django-reverse-url-using-query-args
def url_with_querystring(url, **kwargs):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(kwargs)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)


def jumper(request, host):
    """Actually do jumps."""
    try:
        hostname = validate_hostname(host)
    except ValidationError, e:
        return render(request, 'jump-error.html', {
            'error': e,
            })
    try:
        h = i2phost.objects.get(name=hostname)
    except i2phost.DoesNotExist:
        return render(request, 'jump-unknown.html')
    if h.activated == True:
        key = h.b64hash
    else:
        return redirect(url_with_querystring(reverse('search'), q=hostname))
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
    return render(request, 'jump.html', {
        'url': url,
        })

def index(request):
    return redirect(reverse('index'))
