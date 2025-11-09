from src.exception import CustomException
import logging
import sys
from src import logger  # this imports and configures logging

def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
        # raise our custom exception
        raise CustomException(e, sys)

if __name__ == "__main__":
    logging.info("Starting the test for CustomException and logger setup")

    try:
        result = divide_numbers(10, 0)
        print(result)
    except CustomException as e:
        logging.error(e)
        print("Custom Exception Caught:\n", e)

    logging.info("Program finished.")
