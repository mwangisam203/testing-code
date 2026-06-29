"""Topic 40: working with paths using pathlib."""


from pathlib import Path


current_file = Path(__file__)
project_folder = current_file.parent
notes_file = project_folder / "learning_notes.txt"

print(f"Current file: {current_file.name}")
print(f"Project folder: {project_folder}")
print(f"Notes path: {notes_file}")

# Path thinking:
# Old code often builds paths with string joining.
# `pathlib.Path` lets paths behave like objects instead.

if notes_file.exists():
    print("The notes file exists.")
else:
    print("The notes file does not exist yet.")


python_files = list(project_folder.glob("*.py"))
print(f"Python files found: {len(python_files)}")


# Tip: pathlib can read small text files directly.
if notes_file.exists():
    preview = notes_file.read_text(encoding="utf-8").splitlines()[0]
    print(f"First note preview: {preview}")

# Useful pathlib habits:
# - Path("folder") / "file.txt" builds a path safely.
# - `.exists()` checks if something is there.
# - `.glob("*.py")` searches for matching files.
