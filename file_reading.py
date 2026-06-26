"""Topic 22: reading and writing files."""


filename = "learning_notes.txt"

# File thinking:
# A program's variables disappear when the program ends.
# Files let data survive after Python stops running.
notes = [
    "Functions keep repeated logic in one place.",
    "Classes group data with behavior.",
    "Validation protects the rest of the program.",
]

# `with` opens the file and closes it automatically when the block ends.
# "w" means write mode. It replaces the file if it already exists.
with open(filename, "w", encoding="utf-8") as file:
    for note in notes:
        file.write(note + "\n")

# "r" means read mode.
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        # Lines from a file often include a newline at the end.
        # `strip()` removes that extra whitespace for cleaner printing.
        print(f"Note: {line.strip()}")

# File mode quick guide:
# "r" reads an existing file.
# "w" writes a new file or replaces an old one.
# "a" appends to the end of a file.
