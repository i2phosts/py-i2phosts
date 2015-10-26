from django.contrib.syndication.views import Feed
from django.conf import settings

from pyi2phosts.postkey.models import i2phost
from pyi2phosts.latest.views import get_latest

class AliveHostsFeed(Feed):
    """ Generate RSS feed with all alive hosts """

    title = settings.DOMAIN + ' alive hosts'
    # FIXME: make this URL more dynamic
    link = 'http://' + settings.DOMAIN + '/browse/'
    description = 'All known active hosts inside I2P'

    def items(self):
        return i2phost.objects.filter(activated=True).order_by('name')

    def item_title(self, item):
        return item.name

    def item_link(self, item):
        return 'http://' + item.name + '/?i2paddresshelper=' + item.b64hash

    def item_description(self, item):
        return item.description


class LatestHostsFeed(AliveHostsFeed):
    """ Generate RSS feed with freshly added hosts """

    title = settings.DOMAIN + ' latest hosts'
    # FIXME: make this URL more dynamic
    link = 'http://' + settings.DOMAIN + '/latest/'
    description = 'Freshly added hosts'

    def items(self):
        return get_latest()
