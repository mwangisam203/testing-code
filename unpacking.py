"""Topic 10: unpacking values."""


person = ("Jordan", 24, "Kentucky")
name, age, state = person

numbers = [10, 20, 30, 40]
first, *middle, last = numbers

print(f"{name} is {age} and lives in {state}.")
print(f"First: {first}, middle: {middle}, last: {last}")

# Unpacking assigns several values at once; `*` gathers the extras.
