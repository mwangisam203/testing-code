"""Topic 19: safely managing a resource with `with`."""


# Step 1: __file__ contains the path of the script currently running.
# Step 2: open that path in read mode; read mode is the default.
# Step 3: `with` keeps the file open only while its indented block runs.
with open(__file__, encoding="utf-8") as file:
    # Step 4: readline gets the first line. strip removes its newline.
    first_line = file.readline().strip()

# Step 5: leaving the block closes the file automatically, even if an error
# occurs. The saved string remains available because it is a separate value.
print(first_line)
