from logger import logging
def add(a,b):
    logging.debug("THE ADDITION OPERATION IS TAKING PLACE")
    return a+b

logging.debug("STARTING THE ADDITION FUNCTION")
add(10,15)