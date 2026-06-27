"""Topic 31: practical patterns with lists of dictionaries."""


products = [
    {"name": "notebook", "category": "school", "price": 4.50},
    {"name": "backpack", "category": "school", "price": 35.00},
    {"name": "coffee", "category": "food", "price": 3.25},
    {"name": "sandwich", "category": "food", "price": 8.75},
]


# Pattern 1: filter items.
# Question: Which products cost less than $10?
cheap_products = []
for product in products:
    if product["price"] < 10:
        cheap_products.append(product)

print("Cheap products:")
for product in cheap_products:
    print(f"- {product['name']}")


# Pattern 2: search for one item.
# Question: Where is the backpack?
found_product = None
for product in products:
    if product["name"] == "backpack":
        found_product = product
        break

print(f"Found: {found_product}")


# Pattern 3: group by a key.
# Question: Which products belong to each category?
products_by_category = {}
for product in products:
    category = product["category"]

    if category not in products_by_category:
        products_by_category[category] = []

    products_by_category[category].append(product["name"])

print(products_by_category)

# This list-of-dictionaries shape appears constantly in real Python:
# API results, database rows, CSV files, reports, and user records.
