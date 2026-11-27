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

more_colors = unique_colors | {"purple"}
print(f"Combined colors: {more_colors}")

primary_colors = {"red", "blue", "yellow"}
print(f"Colors not in the original set: {primary_colors - unique_colors}")

print(f"Coordinate pair length: {len(location)}")

print(f"Last unique color alphabetically: {max(unique_colors)}")

new_colors = {"blue", "pink"} - unique_colors
print(f"Colors not already listed: {new_colors}")

print(f"Number of unique colors: {len(unique_colors)}")
