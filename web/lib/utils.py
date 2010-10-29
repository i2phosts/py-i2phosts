import logging

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
		handler = logging.FileHandler(filename)
	else:
		handler = logging.StreamHandler()
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	return logger

