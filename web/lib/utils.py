import sys
import logging
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


def check_logger_options(config):
	""" Check passed config for logger options """
	if 'log_level' in config:
		log_level = config['log_level']
	else:
		sys.stderr.write('"log_level" is missing in config\n')
		sys.exit(1)
	if 'log_file' in config:
		log_file = config['log_file']
	else:
		sys.stderr.write('"log_file is missing in config\n')
		sys.exit(1)
	return (log_file, log_level)
