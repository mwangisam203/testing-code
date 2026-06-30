"""Topic 28: type hints for clearer functions."""


def calculate_area(width: float, height: float) -> float:
    # Type-hint thinking:
    # `width: float` tells readers this function expects a number.
    # `-> float` tells readers this function returns a number.
    #
    # Python still runs dynamically, so hints are not magic guards by default.
    # They are documentation that tools and humans can understand.
    return width * height


def greet_user(name: str, excited: bool = False) -> str:
    # Type hints make the function contract easier to see:
    # input: a name and a yes/no option
    # output: a greeting string
    greeting = f"Hello, {name}"

    if excited:
        return greeting + "!"

    return greeting + "."


def average(numbers: list[float]) -> float:
    # Tip: type hints can describe containers too.
    return sum(numbers) / len(numbers)


room_area = calculate_area(12.5, 10)
message = greet_user("Maya", excited=True)

print(f"Room area: {room_area}")
print(message)
print(f"Average: {average([10, 20, 30])}")

# Important habit:
# Type hints answer, "What kind of value should go here?"
# They make bigger code easier to read before you even run it.

def repeat_word(word: str, times: int) -> str:
    return word * times


print(repeat_word("ha", 3))
