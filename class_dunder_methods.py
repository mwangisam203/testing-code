"""Topic 35: useful dunder methods in classes."""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # `str(book)` is for friendly display to users.
        return f"{self.title} by {self.author}"

    def __repr__(self):
        # `repr(book)` is for debugging and developer clarity.
        # A good repr often looks like code that could recreate the object.
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __eq__(self, other):
        # Equality thinking:
        # Decide what makes two objects "the same" for your program.
        if not isinstance(other, Book):
            return False

        return self.title == other.title and self.author == other.author


book = Book("Python Notes", "Sam")
same_book = Book("Python Notes", "Sam")
different_book = Book("Other Notes", "Sam")

print(str(book))
print(repr(book))
print(book == same_book)
print(book == different_book)

# Dunder means "double underscore."
# These methods let your objects work naturally with Python features.
