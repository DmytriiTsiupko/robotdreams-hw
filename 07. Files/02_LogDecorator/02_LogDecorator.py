
# 2. Write a decorator that will write to a file the name of the function it decorates and write the time of its call.

import datetime


def get_log(func):
    def wraps(*args, **kwargs):
        with open("logs.txt", "a") as file:
            print(f"{func} was called at {datetime.datetime.now()}", file=file)
        result = func(*args, **kwargs)
        return result
    return wraps


@get_log
def power(a, b):
    return a**b


print(power(2, 4))
