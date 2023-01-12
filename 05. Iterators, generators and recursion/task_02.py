# 2. Create a program that will accept a number and print the corresponding number in the Fibonacci sequence using
# iterators

class Fibonacci:

    def __init__(self, max_number):
        self.max_number = max_number
        self.counter = 0
        self.fib1 = 1
        self.fib2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        self.fib = self.fib1

        if self.counter > self.max_number:
            raise StopIteration
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return self.fib


print("### Fibonacci Iterator ###")

while True:
    try:
        input_number = int(input("-> "))

    except ValueError as value:
        print(f"Error: {value}\nPlease, write the number!")

    else:
        fibonacci_sequence = Fibonacci(input_number)
        fibonacci_list = [numb for numb in fibonacci_sequence]

        print(f"{fibonacci_sequence.max_number} number in the Fibonacci sequence: {fibonacci_list[-1]}")


