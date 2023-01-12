# 1. Write your own decorator, the task of which should be to print the name of the function and the time when it was
# called. The decorator should work the same for different functions.
import datetime


def get_log(func):
    def wraps(*args, **kwargs):
        func(*args, **kwargs)
        print(f"{func} was called at {datetime.datetime.now()}.")
    return wraps


@get_log
def power(a, b):
    print(a**b)


@get_log
def plus(a, b):
    print(a + b)


power(1, 2)
plus(1, 2)