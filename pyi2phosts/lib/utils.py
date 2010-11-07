import sys
import logging
import configobj
import validate
import hashlib
import base64

from logging import handlers

def get_logger(filename=None, log_level='debug'):
	""" Prepare logger instance for our scripts """

	# workaround for django
	if hasattr(logging, "web_logger"):
		return logging.web_logger

	LEVELS = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'critical': logging.CRITICAL
	}
	level = LEVELS.get(log_level, logging.NOTSET)
	format = '%(asctime)s %(module)s:%(lineno)d[%(process)d] %(levelname)s: %(message)s'
	formatter = logging.Formatter(format)
	logger = logging.getLogger(__name__)
	logger.setLevel(level)
	if filename:
		handler = logging.handlers.WatchedFileHandler(filename)
	else:
		handler = logging.StreamHandler()
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	# workaround for django
	logging.web_logger = logger

	return logger


def validate_config(config):
	""" Validate configobj config """
	validator = validate.Validator()
	results = config.validate(validator)
	if results != True:
		for (section_list, key, _) in configobj.flatten_errors(config, results):
			if key is not None:
				sys.stderr.write('The "%s" key in the section "%s" failed validation' %
						(key, ', '.join(section_list)))
			else:
				sys.stderr.write('The following section was missing:%s ' %
					', '.join(section_list))
		sys.exit(1)


def get_b32(dest):
	""" Calculate base32 hash from base64 """
	try:
		raw_key = base64.b64decode(dest.encode('utf-8'), '-~')
	except TypeError:
		return 'corrupted_base64_hash'
	else:
		hash = hashlib.sha256(raw_key)
		b32 = base64.b32encode(hash.digest()).lower().replace('=', '')+'.b32.i2p'
		return b32
