from logger import logging

def add(a,b):
    logging.debug("The addition function is taking place")
    return a+b
print(add(5,15))
logging.debug("The addition is done")