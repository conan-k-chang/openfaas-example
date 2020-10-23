import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    logger.info('can you see me?')  # add message here
    return req
