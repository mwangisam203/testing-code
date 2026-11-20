"""Topic 7: sets and tuples."""


colors = ["blue", "red", "blue", "green"]

# Set thinking:
# If the question is "Have I seen this before?" or "What is unique?",
# a set is usually the right tool.
unique_colors = set(colors)

# Tuple thinking:
# Use a tuple for a small group of values that belong together and should not
# be changed accidentally.
location = (36.84, -84.85)

print(f"Unique colors: {unique_colors}")
print(f"Latitude: {location[0]}")

# Sets remove duplicates. Tuples are ordered and cannot be changed.
print(f"Is red included? {'red' in unique_colors}")

warm_colors = {"red", "orange", "yellow"}
favorite_colors = {"blue", "red", "green"}
print(f"Colors in both sets: {warm_colors & favorite_colors}")

print(f"Is red a warm color? {'red' in warm_colors}")
