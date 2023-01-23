# 2. (optional) Write a program that will:
# read text from a file whose name is entered by the user (program argument or input)
# find all emails in the text and change them to *@*.

import re


def encrypting_email(file_name):
    try:
        with open(file_name, "r") as file:
            file_data = file.read()
    except Exception as exp_value:
        print(exp_value)
    else:
        encod_file_data = re.sub(r"(?:^|\s)(\w+[_\w]*@\w+\.\w+[.]?\w+\b)", "*@*", file_data)
        with open(file_name, "w") as file:
            file.write(encod_file_data)
        print("Emails successfully covered!")


encrypting_email(input("Write file name: "))
