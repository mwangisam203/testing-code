"""Topic 39: map, filter, and reduce-style thinking."""


from functools import reduce


prices = [10, 25, 7]

# `map` transforms every item.
# Think: same number of items, different shape/value.
prices_with_tax = list(map(lambda price: price * 1.06, prices))
print(prices_with_tax)


# `filter` keeps only some items.
# Think: maybe fewer items, same original values.
expensive_prices = list(filter(lambda price: price >= 10, prices))
print(expensive_prices)


# `reduce` combines many items into one result.
# Think: list goes in, one final value comes out.
total = reduce(lambda running_total, price: running_total + price, prices, 0)
print(total)


# Example 2: the same transformations using comprehensions and `sum`.
# This is often easier to read in everyday Python.
prices_with_tax_clear = [price * 1.06 for price in prices]
expensive_prices_clear = [price for price in prices if price >= 10]
total_clear = sum(prices)

print(prices_with_tax_clear)
print(expensive_prices_clear)
print(total_clear)


# Example 3: reduce can also keep the "best so far".
# Here the running value is the highest price we have seen.
highest_price = reduce(
    lambda highest, price: price if price > highest else highest,
    prices,
    prices[0],
)
print(f"Highest price: {highest_price}")

# Python often has clearer alternatives:
# - list comprehensions instead of map/filter
# - sum(prices) instead of reduce for adding
# Learn these so you can read them, then choose the clearest option.
