# 3. Create a program that will accept a number and print the corresponding number in the Fibonacci sequence using
# recursion

print("### Fibonacci number ###")

while True:

    def fibonacci_number(number):
        if number <= 1:
            return number
        else:
            return fibonacci_number(number - 1) + fibonacci_number(number - 2)

    try:
        input_number = int(input("-> "))
        print(f"{input_number} number in the Fibonacci sequence: {fibonacci_number(input_number)}")
    except:
        print("Please, write the number!")