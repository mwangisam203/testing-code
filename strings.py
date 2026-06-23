"""Topic 6: strings are immutable."""


message = "  learning Python  "

clean_message = message.strip().title()
words = clean_message.split()

print(clean_message)
print(words)

# String methods create new strings; they do not change the original.
print(f"Original: {message!r}")
