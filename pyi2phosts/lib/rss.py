#!/usr/bin/env python2.6

from django.contrib.syndication.views import Feed
from pyi2phosts.postkey.models import i2phost

import settings

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
