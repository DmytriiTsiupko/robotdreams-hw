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
        # open file for reading
        with open(file_name, "r") as file:
            file_data = file.read()
    except Exception as exp_value:
        print(exp_value)

    else:
        # finding emails in file
        emails = re.findall(r"(?:^|\s)(\w+[_\w]*@\w+\.\w+[.]?\w+\b)", file_data)
        try:
            for mail in emails:
                # encode found emails
                encod_mail = f"{mail[0]}***@***{mail[-1]}"
                # create text with encoded emails
                file_data = file_data.replace(mail, encod_mail)
        except Exception as exp_value:
            print(exp_value)
        else:
            try:
                with open("emails.txt", "w") as file:
                    # write new text to file
                    file.write(file_data)
                    print("Emails successfully encoded!\n")
            except Exception as exp_value:
                print(exp_value)


while True:
    encrypting_email(input("Write file name: "))
