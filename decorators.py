"""Topic 18: wrapping a function with a decorator."""


def announce(function):
    # Step 1: `function` receives the original `study` function.
    # Step 2: define a wrapper that adds work before and after it.
    def wrapper():
        print("Starting...")
        function()  # Call the original study function here.
        print("Finished!")

    # Step 3: return the wrapper itself. The parentheses are omitted because
    # we do not want to run it yet.
    return wrapper


# Step 4: @announce is equivalent to: study = announce(study)
@announce
def study():
    print("Practicing Python")


# Step 5: `study` now refers to wrapper, so all three lines are printed.
study()


def trace(function):
    # Deeper decorator thinking:
    # Real functions often have parameters, so a useful wrapper should accept
    # any positional arguments (`*args`) and keyword arguments (`**kwargs`).
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}...")
        result = function(*args, **kwargs)
        print(f"{function.__name__} returned {result!r}")
        return result

    return wrapper


@trace
def add_numbers(first, second):
    return first + second


sum_result = add_numbers(3, 4)
print(f"Final sum: {sum_result}")


print(f"Wrapped function name: {add_numbers.__name__}")
# Tip: simple decorators can hide the original function name.
# Later, `functools.wraps` fixes that for production-quality decorators.

# Decorator thinking:
# Use a decorator when you want to add the same extra behavior around many
# functions, like logging, timing, checking permission, or printing status.
# `*args` and `**kwargs` let the decorator work with many function shapes.

@trace
def shout(text):
    return text.upper()


print(shout("decorators"))
