import time

from .stock_room import bubble_sort, merge_sort, quick_sort
from .warehouse import delivery


# Measure sort time
def measure_sort_time(sort_function, items):
    start_time = time.time()
    sort_function(items)
    end_time = time.time()
    return end_time - start_time


# Find the fastest sorting function
def get_fastest_sort_function():
    if not delivery:
        raise ValueError("Delivery list is empty. No items to sort.")

    sort_functions = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
    }

    times = {}
    for name, sort_function in sort_functions.items():
        items = delivery.copy()  # Copy the delivery list to avoid modifying the original data
        sort_time = measure_sort_time(sort_function, items)
        times[name] = sort_time

    # Find the fastest sorting function
    fastest_sort_name = min(times, key=times.get)

    # Print execution times and the fastest sorting algorithm
    print("Execution time for each algorithm:")
    for name, time_taken in times.items():
        print(f"{name}: {time_taken:.6f} seconds")

    print(f"\nThe fastest sorting algorithm is: {fastest_sort_name}.")

    return sort_functions[fastest_sort_name]


# Export the fastest sorting function for use in other files
fastest_sort_function = get_fastest_sort_function()
