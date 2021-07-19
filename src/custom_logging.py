import logging
import datetime


# I assume decorators or something would improve this module


def timestamp():
	now = datetime.datetime.now()
	return f"{now.month}/{now.day}-{now.hour}:{now.minute}:{now.second}"


def filename_timestamp():
	now = datetime.datetime.now()
	return f"{now.month}-{now.day}-{now.hour}-{now.minute}"


def log_debug(message, source='', display=True):
	if display:
		print(f"(DEBUG){timestamp()}{source} -- {message}")
	logging.debug(message)


def log_header(message):
	print(f'====================================== {message}\n{timestamp()}\n')


def log_sub_header(message):
	print(f'================ {message}\n{timestamp()}\n')


def config_log():
	logging.basicConfig(filename=f"./logs/{filename_timestamp()}.log", level=logging.DEBUG, format='%(asctime)s - %(message)s')


def log_info(message, source='', display=True):
	# skip a few spaces and print a header if provided
	if display:
		print(f"(INFO){timestamp()}{source} -- {message}")
	logging.info(message)


def log_warning(message, source='', display=True):
	if display:
		print(f"(WARNING){timestamp()}{source} -- {message}")
	logging.warning(message)


def log_studio(message, source='', display=True):
	if display:
		print(f"(STUDIO){timestamp()}{source} -- {message}")
	logging.info(f"STUDIO: {message}")


def log_rhythm(message, source='', display=True):
	if display:
		print(f"(RHYTHM){timestamp()}{source} -- {message}")
	logging.info(f"(RHYTHM): {message}")
	

config_log()
