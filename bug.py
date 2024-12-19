def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but not always caught
    else:
        return x + 5

# Example demonstrating the error
result = function_with_uncommon_error(0)
print(result)