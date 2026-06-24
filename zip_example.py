"""Topic 16: combining sequences with zip."""


names = ["Ava", "Noah", "Mia"]
scores = [91, 84, 96]

# Step 1: Both lists store related data in matching positions.
# Step 2: zip creates pairs: ("Ava", 91), ("Noah", 84), and so on.
# Step 3: the loop unpacks one pair into `name` and `score` each time.
for name, score in zip(names, scores):
    # Step 4: the f-string displays the two values from the current pair.
    print(f"{name} scored {score}")

# Important: zip stops when the shortest sequence runs out of items.
