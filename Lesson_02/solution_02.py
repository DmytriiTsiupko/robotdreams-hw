
def check_type(input_string):

    print(f"Input string: {input_string}")
    uniq_chars = {}

    # create dictionary of uniq chars
    for uniq_char in input_string:

        if uniq_char in uniq_chars:
            uniq_chars[uniq_char] += 1
        else:
            uniq_chars[uniq_char] = 1

    # cleare input string from invalid symbols
    cleared_string = "".join(char for char in input_string if char.isalnum())

    # check the type of cleared input string
    if cleared_string.isalpha() == True:
        print(f"Data type: strings\nString lenght: {len(input_string)}")

    elif cleared_string.isdigit() == True:
        print("Data type: numeric.")

        if int(cleared_string) % 2 == 0:
            print(f"{cleared_string} is even number.")

        else:
            print(f"{cleared_string} is odd number.")

    elif cleared_string.isalnum() == True:
        print("Data type: strings and numerics")

    else:
        print("Data type: input string is empty or contain invalid chars")


    print(f"Uniq chars: {uniq_chars}")


user_input = input("Please, write something: ")

check_type(user_input)