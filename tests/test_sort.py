import pytest
from sort.performance_analysis import get_fastest_sort_function
from sort.stock_room import bubble_sort, merge_sort, quick_sort
from sort.warehouse import colors_order, delivery, items_generator, items_number, sizes_order


# Test for items_generator function
def test_items_generator():
    # Generate a sample item
    result = items_generator()

    # Check if the result is a dictionary
    assert isinstance(result, dict), "items_generator should return a dictionary"

    # Check if the result has valid 'color' and 'size' keys
    assert result["color"] in colors_order, "Color is not valid"
    assert result["size"] in sizes_order, "Size is not valid"

    color = result["color"]
    size = result["size"]

    # Check if the color maps to an integer in colors_order
    assert isinstance(
        colors_order[color], int
    ), f"Color '{color}' should map to an integer in colors_order"

    # Check if the size maps to an integer in sizes_order
    assert isinstance(
        sizes_order[size], int
    ), f"Size '{size}' should map to an integer in sizes_order"


# Test to check if the delivery list has the expected length
def test_delivery_length():
    assert len(delivery) == items_number, f"Delivery list should contain {items_number} items"


# Test to check the content of each item in the delivery list
def test_delivery_content():
    for item in delivery:
        # Check if each item is a dictionary
        assert isinstance(item, dict), "Each item in the delivery should be a dictionary"

        # Check if each item has the keys 'color' and 'size'
        assert "color" in item, "Each item should contain the key 'color'"
        assert "size" in item, "Each item should contain the key 'size'"

        color = item["color"]
        size = item["size"]

        # Check if the color is in the predefined colors_order
        assert color in colors_order, f"Color '{color}' in delivery is not in colors_order"

        # Check if the size is in the predefined sizes_order
        assert size in sizes_order, f"Size '{size}' in delivery is not in sizes_order"

        # Check if the color maps to an integer in colors_order
        assert isinstance(
            colors_order[color], int
        ), f"Color '{color}' should map to an integer in colors_order"

        # Check if the size maps to an integer in sizes_order
        assert isinstance(
            sizes_order[size], int
        ), f"Size '{size}' should map to an integer in sizes_order"


# Test to check behavior with empty delivery list
def test_empty_delivery():
    # Backup the original delivery list
    original_delivery = delivery.copy()

    try:
        # Empty the delivery list
        delivery.clear()

        # Check if the function raises an error for empty delivery
        with pytest.raises(ValueError, match="Delivery list is empty. No items to sort."):
            get_fastest_sort_function()
    finally:
        # Restore the original delivery list
        delivery.extend(original_delivery)


# Test the sorting algorithms to ensure they sort correctly
def test_sorting_algorithms():
    items = delivery.copy()

    # Test Bubble Sort
    sorted_items_bubble = bubble_sort(items.copy())
    assert sorted_items_bubble == sorted(
        items, key=lambda x: (colors_order[x["color"]], sizes_order[x["size"]])
    ), "Bubble sort did not sort correctly"

    # Test Quick Sort
    sorted_items_quick = quick_sort(items.copy())
    assert sorted_items_quick == sorted(
        items, key=lambda x: (colors_order[x["color"]], sizes_order[x["size"]])
    ), "Quick sort did not sort correctly"

    # Test Merge Sort
    sorted_items_merge = merge_sort(items.copy())
    assert sorted_items_merge == sorted(
        items, key=lambda x: (colors_order[x["color"]], sizes_order[x["size"]])
    ), "Merge sort did not sort correctly"


# Test the performance analysis to ensure it identifies the fastest sorting function
def test_performance_analysis():
    # Retrieve the fastest sorting function
    fastest_sort_function = get_fastest_sort_function()

    # Check if the returned object is callable (a function)
    assert callable(fastest_sort_function), "The fastest_sort_function should be callable"

    # Check if the function returns a correctly sorted list
    sorted_delivery = fastest_sort_function(delivery.copy())
    assert sorted_delivery == sorted(
        delivery, key=lambda x: (colors_order[x["color"]], sizes_order[x["size"]])
    ), "The fastest sort function did not sort correctly"
