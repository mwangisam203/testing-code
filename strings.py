"""Topic 6: strings are immutable."""


message = "  learning Python  "

# String thinking:
# User input is often messy, so clean it before comparing or saving it.
# `strip()` removes outer spaces, then `title()` capitalizes words.
clean_message = message.strip().title()

# `split()` turns one string into a list of smaller strings.
words = clean_message.split()

print(clean_message)
print(words)

# String methods create new strings; they do not change the original.
print(f"Original: {message!r}")
# The `!r` shows hidden spaces, which is useful when debugging text.
