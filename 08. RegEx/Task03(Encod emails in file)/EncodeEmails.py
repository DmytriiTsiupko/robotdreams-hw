# 3. (optional) Write a program that will:
#
# read text from a file whose name is entered by the user (program argument or input)
#
# find all emails in the text and change them to X***@****X, where X should be replaced by the first and last letters
# of the real address, and all other text should be replaced by *. The number of * does not necessarily have to
# correspond to the number of replaced characters


import re


def encrypting_email(file_name):
    try:
        with open(file_name, 'r') as file:   # open file for reading
            file_data = file.read()
    except Exception as exp_value:
        print(exp_value)

    else:
        emails = re.findall(r"(?:^|\s)(\w+[_\w]*@\w+\.\w+[.]?\w+\b)", file_data)     # finding emails in file
        try:
            for mail in emails:
                encod_mail = f"{mail[0]}***@***{mail[-1]}"               # encode found emails
                file_data = file_data.replace(mail, encod_mail)              # create text with encoded emails
        except Exception as exp_value:
            print(exp_value)
        else:
            try:
                with open("emails.txt", 'w') as file:
                    file.write(file_data)             # write new text to file
                    print("Emails successfully encoded!\n")
            except Exception as exp_value:
                print(exp_value)


while True:
    encrypting_email(input("Write file name: "))


