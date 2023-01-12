# Write a try ... else ... else ... finally construction that will do exactly what previous task's context manager did.

def power(numb_1, numb_2):
    print(numb_1**numb_2)


try:
    print("==========")
    a: int = int(input())
    b: int = int(input())

except Exception as value_error:
    print({value_error})

else:
    power(a, b)

finally:
    print("==========")
