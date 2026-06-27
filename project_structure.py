"""Topic 36: thinking about project structure."""


# Project-structure thinking:
# As programs grow, every file should have a job.
#
# A small Python project might look like this:
#
# project/
#   main.py              -> starts the program
#   models.py            -> classes / dataclasses
#   helpers.py           -> reusable small functions
#   data/                -> files the program reads or writes
#   tests/               -> tests that prove behavior
#
# You do not need this structure for every tiny script.
# The goal is to know when a file is getting too crowded.


def describe_file_role(filename):
    if filename == "main.py":
        return "starts the program"
    if filename.endswith("_helpers.py"):
        return "stores reusable helper functions"
    if filename.startswith("test_"):
        return "checks that code works"

    return "holds one focused topic or feature"


files = ["main.py", "modules_helpers.py", "test_budget.py", "classes.py"]

for filename in files:
    print(f"{filename}: {describe_file_role(filename)}")

# A useful rule:
# If you cannot explain a file's job in one sentence, it may be doing too much.
