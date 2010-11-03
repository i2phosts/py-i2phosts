#!/usr/bin/env python2.6

import re

from django.core.exceptions import ValidationError

from postkey.models import i2phost


def validate_hostname(data):
	"""
	Here we do hostname validation as described in
	http://www.i2p2.i2p/naming.html and some additional checks
	described in http://zzz.i2p/topics/739
	"""
	# convert hostname to lowercase and strip leading and trailing whitespaces
	data = data.lower().strip()
	# do lenght check here for avoiding django.db.utils.DatabaseError exceptions
	# when trying to add too long hostname with py-i2phosts-injector
	if len(data) > 67:
		raise ValidationError('Too long hostname (should be 67 chars max)')
	# Must end with '.i2p'.
	if re.match(r'.*\.i2p$', data) == None:
		raise ValidationError('Hostname doesn\'t ends with .i2p')
	# Base 32 hostnames (*.b32.i2p) are not allowed
	if re.match(r'.*\.b32\.i2p$', data):
		raise ValidationError('Base32 hostnames are not allowed')
	# prevent common errors
	if re.match(r'\.i2p$', data):
		raise ValidationError('Incomplete hostname')
	if re.match(r'^http:/', data):
		raise ValidationError('Do not paste full URL, just domain')
	# Must not contain '..'
	if re.search(r'\.\.', data):
		raise ValidationError('".." in hostname')
	# Allow only 4ld domains and below
	if data.count('.') > 3:
		raise ValidationError('Subdomains deeper than 4LD are not allowed')
	# Must contain only [a-z] [0-9] '.' and '-'
	h = re.match(r'([a-z0-9.-]+)\.i2p$', data)
	if h == None:
		raise ValidationError('Illegal characters in hostname')
	else:
		namepart = h.groups()[0]
	# Must not start with '.' or '-'
	if re.match(r'^\.|-', namepart):
		raise ValidationError('Hostname must not starts with "." or "-"')
	# Must not contain '.-' or '-.' (as of 0.6.1.33)
	if re.search(r'(\.-)|(-\.)', namepart):
		raise ValidationError('Hostname contain ".-" or "-."')
	# Must not contain '--' except in 'xn--' for IDN
	if re.search(r'(?<!^xn)--', namepart) and re.search(r'(?<!\.xn)--', namepart):
		raise ValidationError('Hostname contain "--" and it\'s not an IDN')
	# Certain hostnames reserved for project use are not allowed
	if re.search(r'(^|\.)(proxy|router|console|b32|b64)$', namepart):
		raise ValidationError('Trying to use reserved hostname')
	# Block various localhost.* in addition
	if re.match(r'^localhost($|\..*$)', namepart):
		raise ValidationError('localhost.* not allowed')
	return data


def validate_b64hash(data, check_uniq=True):
	"""
	Base64 hash validation
	"""
	# strip leading and trailing whitespaces
	data = data.strip()
	length = len(data)
	# check for b32 address misuse
	if re.match(r'.*\.b32\.i2p$', data):
		raise ValidationError('You should paste base64 hash, not a base32!')
	# fail if contains .i2p= (full foo.i2p=key)
	if re.search(r'\.i2p=', data):
		raise ValidationError('Do not paste full hosts.txt entry! Only base64 hash are needed')
	# check for pasting router hash
	if length == 44:
		raise ValidationError('Do not paste router hash! Go to i2ptunnel page and \
				find a destination hash')
	# Minimum key length 516 bytes
	if length < 516:
		raise ValidationError('Specified base64 hash are less than 516 bytes')
	# Maximum key length 616 bytes
	if length > 616:
		raise ValidationError('Specified base64 hash are bigger than 616 bytes')
	# keys with cert may ends with anything, so check is relaxed
	if length > 516 and re.match(r'[a-zA-Z0-9\-~]+$', data) == None:
		raise ValidationError('Invalid characters in base64 hash')
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
			raise ValidationError('Corrupted base64 hash')
	# base64-i2p
	if length == 516 and re.match(r'[a-zA-Z0-9\-~]+AA$', data) == None:
		raise ValidationError('Invalid base64 hash')
	if check_uniq == True:
		# Avoid adding non-unique hashes
		qs = i2phost.objects.filter(b64hash=data)
		if qs.exists():
			raise ValidationError('Base64 hash must be unique')
	return data


def validate_i2purl(data):
	""" Basic I2P URL validator """
	# convert to lowercase and strip leading and trailing whitespaces
	data = data.lower().strip()
	# check for http://, .i2p in domain and GET validity
	if re.match(r'^http://(?:.+?\.i2p)(?:/?|[/?]\S+)$', data) == None:
		raise ValidationError('Bad I2P url')
