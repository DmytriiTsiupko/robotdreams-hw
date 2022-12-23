
def check_type(input_string):

    print(f"Input string: {input_string}")
    uniq_chars = {}

    # create dictionary of uniq chars
    for uniq_char in input_string:

        if uniq_char in uniq_chars:
            uniq_chars[uniq_char] += 1
        else:
            uniq_chars[uniq_char] = 1


    # check the type of input string
    if input_string == "":
        print("Data type: input string is empty")

    elif input_string.isdigit() == True:
        print("Data type: digit.")

        if int(input_string) % 2 == 0:
            print(f"{input_string} is even number.")

        else:
            print(f"{input_string} is odd number.")

    else:
        print(f"Data type: string\nString lenght: {len(input_string)}")


    print(f"Uniq chars: {uniq_chars}")


user_input = input("Please, write something: ")

check_type(user_input.strip())