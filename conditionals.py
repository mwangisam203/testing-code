"""Topic 5: conditionals and comparison order."""


temperature = 28

if temperature >= 30:
    message = "It is hot."
elif temperature >= 20:
    message = "It is warm."
else:
    message = "It is cold."

print(message)

# Python stops at the first condition that is True.
