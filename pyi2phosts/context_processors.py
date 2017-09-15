from django.conf import settings

from pyi2phosts.lib.utils import get_b32


def global_settings(request):
    # return any necessary values
    return {
        'LANGUAGES': settings.LANGUAGES,
        'title': settings.SITE_NAME,
        'domain': settings.DOMAIN,
        'b64': settings.MY_B64,
        'b32': get_b32(settings.MY_B64),
        'day_count': settings.LATEST_DAY_COUNT,
        'hosts_count': settings.LATEST_HOSTS_COUNT
    }
