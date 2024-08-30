import random

# Predefined orders for colors and sizes
colors_order = {
    "red": 1,
    "orange": 2,
    "yellow": 3,
    "green": 4,
    "blue": 5,
    "indigo": 6,
    "violet": 7,
}

sizes_order = {"XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5}


def items_generator():
    return {
        "color": random.choice(list(colors_order.keys())),
        "size": random.choice(list(sizes_order.keys())),
    }


# Number of items for the delivery
items_number = 1000
# Generate a delivery
delivery = [items_generator() for i in range(items_number)]
