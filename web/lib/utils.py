import sys
import logging
import configobj
import validate

from logging import handlers

def get_logger(filename=None, log_level='debug'):
	""" Prepare logger instance for our scripts """

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
