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

# Updating JSON thinking:
# Loading JSON gives us normal Python data again, so we can change it like any
# other dictionary or list.
loaded_profile["skills"].append("json")
loaded_profile["last_topic"] = "saving data"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(loaded_profile, file, indent=2)

print("Updated profile saved.")


required_keys = ["name", "skills", "is_learning"]
for key in required_keys:
    if key not in loaded_profile:
        print(f"Missing key: {key}")

# JSON supports simple data types:
# strings, numbers, booleans, None, lists, and dictionaries.
# It does not automatically save custom class objects unless you convert them.
# The common cycle is: load data, change it in Python, then save it again.
