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
