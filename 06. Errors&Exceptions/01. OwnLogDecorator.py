# 1. Write your own decorator, the task of which should be to print the name of the function and the time when it was
# called. The decorator should work the same for different functions.
import datetime


def get_log(func):
    def wraps(*args, **kwargs):
        print(f"{func} was called at {datetime.datetime.now()}.")
        result = func(*args, **kwargs)
        return result
    return wraps


@get_log
def power(a, b):
    return a**b


@get_log
def plus(a, b):
    return a + b


print(power(1, 2))
print(plus(1, 2))
