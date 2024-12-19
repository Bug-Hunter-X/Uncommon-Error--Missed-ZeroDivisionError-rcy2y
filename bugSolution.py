import logging


def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 5
    except ZeroDivisionError as e:
        logging.exception(f"Error while executing function: {e}")
        return None  # Or raise the exception, depending on your needs

# Example demonstrating the error handling
result = function_with_uncommon_error(0)
print(result)
result = function_with_uncommon_error(5)
print(result)

#Setting up logging
logging.basicConfig(level=logging.ERROR, filename='error.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
