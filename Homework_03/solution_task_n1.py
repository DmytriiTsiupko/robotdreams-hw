# 1. Create a program that will expect the user to enter text and output information for each typed character:
#
# - this "number" + what it is (even, odd),
# - this is a "string" + what is it (uppercase or lowercase),
# - is a "symbol"


def check_chars(input_string):

    for char in input_string:

        if char.isdigit():
            print(f"{char} is a digit", end=" ")

            if int(char) % 2 == 0:
                print(f"and it's an even number")
            else:
                print(f"and it's an odd number")\

        elif char.isalpha():
            print(f"{char} is a string", end=" ")

            if char.isupper():
                print("and it's a capital letter")
            else:
                print("and it's a small letter")

        else:
                print(f"{char} is a symbol")

input_string = input("Please, write something: ")
check_chars(input_string)