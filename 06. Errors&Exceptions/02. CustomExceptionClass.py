# 2. Write a custom Exception class, MyCustomException, which should report "Custom exception is occurred".

class MyCustomException(Exception):
    def __init__(self, massage="Custom exception is occurred"):
        self.massage = massage
        super().__init__(self.massage)


try:
    raise MyCustomException()

except MyCustomException as value:
    print(f"{value}")
