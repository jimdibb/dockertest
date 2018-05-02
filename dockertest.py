
import sys
import logging

logging.basicConfig(format='%(message)s', level=logging.DEBUG)
logging.info("test started")

logging.info(str(sys.argv))
print (len(sys.argv))
print (str(sys.argv))