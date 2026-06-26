"""Topic 24: modules and imports."""


from modules_helpers import calculate_average, format_money


def main():
    # `main` holds the "run the script" behavior.
    # This keeps the file import-friendly because importing it will not
    # immediately run the whole lesson.
    scores = [90, 84, 100]
    average = calculate_average(scores)

    print(f"Average score: {average:.1f}")
    print(f"Wallet balance: {format_money(42.5)}")


if __name__ == "__main__":
    # This block runs only when this file is executed directly:
    # python3 modules_imports.py
    #
    # If another file imports from this file, Python skips this block.
    main()

# Module thinking:
# When one file gets too crowded, move reusable functions into another file.
# Then import only the names you need.
#
# In this example:
# - `modules_helpers.py` stores reusable helper functions.
# - `modules_imports.py` uses those helpers to solve a small problem.
#
# This is one of the first steps toward organizing bigger projects.
# The `if __name__ == "__main__"` pattern separates reusable code from script
# behavior. It looks weird at first, but it becomes very normal in Python.
