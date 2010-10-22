#!/usr/bin/env python2.6

import re

from django import forms
from web.postkey.models import i2phost


def validate_hostname(data):
	"""
	Here we do additional hostname validation as described in
	http://www.i2p2.i2p/naming.html
	"""
	# convert hostname to lowercase and strip leading and trailing whitespaces
	data = data.lower().strip()
	# Must end with '.i2p'.
	if re.match(r'.*\.i2p$', data) == None:
		raise forms.ValidationError('Hostname doesn\'t ends with .i2p')
	# Base 32 hostnames (*.b32.i2p) are not allowed
	if re.match(r'.*\.b32\.i2p$', data):
		raise forms.ValidationError('Base 32 hostnames are not allowed')
	# Must not contain '..'
	if re.search(r'\.\.', data):
		raise forms.ValidationError('".." in hostname')
	# Must contain only [a-z] [0-9] '.' and '-'
	h = re.match(r'([a-z0-9.-]+)\.i2p$', data)
	if h == None:
		raise forms.ValidationError('Illegal characters in hostname')
	else:
		namepart = h.groups()[0]
	# Must not contain '.-' or '-.' (as of 0.6.1.33)
	if re.search(r'(\.-)|(-\.)', namepart):
		raise forms.ValidationError('Hostname contain ".-" or "-."')
	# Must not contain '--' except in 'xn--' for IDN
	if re.search(r'(?<!^xn)--', namepart):
		raise forms.ValidationError('Hostname contain "--" and it\'s not an IDN')
	# Certain hostnames reserved for project use are not allowed
	if re.search(r'(^|\.)(proxy|router|console)$', namepart):
		raise forms.ValidationError('Trying to use reserved hostname')
	return data


def validate_b64hash(data, check_uniq=True):
	"""
	Base64 hash validation
	"""
	length = len(data)
	# Minimum key length 516 bytes
	if length < 516:
		raise forms.ValidationError('Specified base64 hash are less than 516 bytes')
	# Maximum key length 616 bytes
	if length > 616:
		raise forms.ValidationError('Specified base64 hash are bigger than 616 bytes')
	# keys with cert may ends with anything, so check is relaxed
	if length > 516 and re.match(r'[a-zA-Z0-9\-~]+$', data) == None:
		raise forms.ValidationError('Invalid characters in base64 hash')
	# base64-validity test
	if length > 516:
		# we need temporary variable here to avoid modifying main "data"
		test_data = data
		# add pad-characters needed for proper decoding cos i2p does not
		for i in range(4):
			quanta, leftover = divmod(len(test_data), 4)
			if leftover:
				test_data += '='
			else:
				break
		# if more than 2 pad chars were added, raise an error
		if i > 2:
			raise forms.ValidationError('Corrupted base64 hash')
	# base64-i2p
	if length == 516 and re.match(r'[a-zA-Z0-9\-~]+AA$', data) == None:
		raise forms.ValidationError('Invalid base64 hash')
	if check_uniq == True:
		# Avoid adding non-unique hashes
		qs = i2phost.objects.filter(b64hash=data)
		if qs.exists():
			raise forms.ValidationError('Base64 hash must be unique')
	return data
