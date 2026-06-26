"""Topic 23: saving structured data with JSON."""


import json


profile = {
    "name": "Maya",
    "skills": ["functions", "classes", "loops"],
    "is_learning": True,
}

filename = "profile.json"

# JSON thinking:
# Python dictionaries are great while a program is running.
# JSON is a common text format for saving or sharing that dictionary-shaped data.
with open(filename, "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=2)

with open(filename, "r", encoding="utf-8") as file:
    loaded_profile = json.load(file)

print(f"{loaded_profile['name']} is learning:")

for skill in loaded_profile["skills"]:
    print(f"- {skill}")

# JSON supports simple data types:
# strings, numbers, booleans, None, lists, and dictionaries.
# It does not automatically save custom class objects unless you convert them.
