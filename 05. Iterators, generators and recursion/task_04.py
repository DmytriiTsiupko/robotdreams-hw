# 4. Write a program that will return the factorial of the entered
#    number using recursion

print("### Factorial (max 998)###")

while True:

    def get_factorial(input_number):
        if input_number == 1:
            return 1
        else:
            return input_number * get_factorial(input_number - 1)

    try:
        number = int(input("-> "))

    except ValueError as value:
        print(f"Error: {value}\nPlease, write the number!")

    else:
        print(f"Factorial of {number} is {get_factorial(number)}")
