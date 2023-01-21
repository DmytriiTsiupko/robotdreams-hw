# 3. In the previously written custom Exception, add a record of the error and the time of its occurrence to the file.
from datetime import datetime


class MyCustomException(Exception):
    def __init__(self, massage="Custom exception is occurred"):
        self.massage = massage
        super().__init__(self.massage)
        with open("logs.txt", "a") as file:
            print(f"MyCustomException was called at {datetime.now()}", file=file)


# try:
#     raise MyCustomException()
#
#   except MyCustomException as value:
#     print(f"{value}")
