from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'LANGUAGES': settings.LANGUAGES,
        'title': settings.SITE_NAME,
    }
