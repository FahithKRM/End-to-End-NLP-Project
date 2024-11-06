from hate.logger import logging ## for logging
from hate.exception import CustomException ## for exception
import sys


#logging.info("Welcome to our Project") ## for logging

## for exception
try:
    a = 7/"0"

except Exception as e:
    raise CustomException(e, sys) from e