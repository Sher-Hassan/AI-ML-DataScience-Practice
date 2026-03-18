import logging

## Logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[  # Handlers are the components that determine where your log messages actually go.
        logging.FileHandler("app1.log"),  # Writes log messages to app1.log file
        logging.StreamHandler()  # Outputs log messages to console (stdout)
    ]
)

## Creating modules/loggers

logger = logging.getLogger("ArithemeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,15)
subtract(25,3)
multiply(10,3)
divide(80,4)