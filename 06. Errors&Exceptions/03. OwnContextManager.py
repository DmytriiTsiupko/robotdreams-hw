# 3. Write your own context manager whose task will be to print "==========" - 10 characters are equal before code
# execution and after code execution, thus highlighting the block of code with equals characters.

class OwnContextManager:
    def __init__(self, chars: str = "=========="):
        self.chars = chars

    def __enter__(self):
        print(self.chars)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.chars)


def power(a, b):
    print(a**b)


with OwnContextManager():
    try:
        power(a=int(input()), b=int(input()))
    except Exception as error_value:
        print(f"{error_value}")

