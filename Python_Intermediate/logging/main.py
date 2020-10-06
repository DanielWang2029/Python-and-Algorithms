

import logging

logger = logging.getLogger(__name__)

# create handler
stream = logging.StreamHandler()
file = logging.FileHandler('logging/file.log')

# level and format
stream.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(stream)
logger.addHandler(file)

logger.warning('this is a warning')
logger.error('this is an error')
