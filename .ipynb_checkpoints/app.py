import logging

# Properly configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

# Create a named logger
logger = logging.getLogger("ArithmeticApp")

# Arithmetic functions with logging
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result

def subtract(a, b):  # fixed spelling
    result = a - b
    logger.debug(f"Subtracting {a} and {b} to get {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} and {b} to get {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None

# Run some test operations
add(10, 15)
subtract(20, 5)
multiply(4, 5)
divide(20, 4)
divide(10, 0)  # triggers error logging