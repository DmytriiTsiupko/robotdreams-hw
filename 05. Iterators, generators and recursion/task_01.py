# 1. Create a program that will receive a number and print the corresponding number in the Fibonacci list using
# generators
print("### Fibonacci Generator ###")
while True:
    def get_fibonacci(number):   # create generator
        fib1 = fib2 = 1
        for i in range(number):
            yield fib1
            fib1, fib2 = fib2, fib1 + fib2


    try:
        input_number = int(input("-> "))

    except ValueError as value:
        print(f"Error: {value}\nPlease, write the number!")

    else:
        generator_fibonacci = get_fibonacci(input_number)
        fibonacci_list = list(generator_fibonacci)

        print(f"{input_number} number in the Fibonacci sequence: {fibonacci_list[-1]}\n")
