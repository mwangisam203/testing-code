"""Topic 33: command-line arguments with sys.argv."""


import sys


# Command-line thinking:
# Sometimes you want to run the same script with different values:
# python3 command_line_args.py Maya
#
# `sys.argv` is the list of words passed to the script.
# Item 0 is always the script name.
if len(sys.argv) >= 2:
    name = sys.argv[1]
else:
    name = "friend"

print(f"Hello, {name}!")


def get_mode(arguments):
    # Small helper functions make command-line parsing easier to test.
    if "--loud" in arguments:
        return "loud"

    return "normal"


mode = get_mode(sys.argv)

if mode == "loud":
    print("PYTHON IS FUN!")
else:
    print("Python is fun.")

# Bigger projects often use `argparse`, but `sys.argv` is the simple starting
# point for understanding how terminal input reaches your script.
