#!/usr/bin/python

import os
import sys

# django setup
DJANGO_SETTINGS_MODULE = 'settings'
DJANGO_PROJECT_PATH = os.path.dirname(sys.argv[0]) + '/web'
sys.path.insert(1, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
from web.postkey.models import i2phost

# result hosts.txt
hostsfile = 'hosts.txt'

f = open(hostsfile, 'w')
# select name and hash for all activated hosts
l = i2phost.objects.filter(activated=True).values('name', 'b64hash')
for entry in l:
	f.write(entry['name'] + '=' + entry['b64hash'])
f.close()
