"""Topic 1: loops and input validation."""

import math


while True:
    try:
        number = float(input("Enter a number that is 0 or greater: "))

        if number < 0:
            print("A square root needs a non-negative number.")
            continue

        break
    except ValueError:
        print("Please enter numbers only.")

square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root:.2f}")
