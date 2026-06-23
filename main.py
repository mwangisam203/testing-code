import math

y = True
while y == True:
    x = input("Please Enter a number: ")
    try:
        x = float(x)
        break

    except ValueError:
        print("Invalid Choice")

y = math.sqrt(x)
print(f"The root of {x} is {y:.2f}")



while True:
    try:
        user_input = float(input("Please enter number: ")) # ask the user for a number
        if user_input > 0:
            #print("Enter 0 or a positive Int")  # square root needs non-negative numbers
            #continue
            break  #stop the loop if the input is valid


    except ValueError:
        print("Enter a valid choice(numbers only !!)") # handle non-numeric input

square_root = math.sqrt(user_input) 

print(f"the root of {user_input} is {square_root}")