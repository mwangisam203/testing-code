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

# Python often has clearer alternatives:
# - list comprehensions instead of map/filter
# - sum(prices) instead of reduce for adding
# Learn these so you can read them, then choose the clearest option.
