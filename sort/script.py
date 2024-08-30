import os
import sys

# Add the main project directory to the module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sort.performance_analysis import fastest_sort_function
from sort.warehouse import delivery


def sort_delivery(sorted_list):
    # Prepare to summarize
    total_items = len(sorted_list)
    print(f"\nA total of {total_items} items arrived.")
    print("After sorting, the distribution is as follows:\n")

    # Create a dictionary to organize the sorted list by color
    sorted_by_color = {}

    # Iterate through the sorted_list to populate the sorted_by_color dictionary
    for item in sorted_list:
        color = item["color"]
        size = item["size"]

        if color not in sorted_by_color:
            sorted_by_color[color] = {
                "items": [],  # List of items for the color
                "size_counts": {},  # Dictionary to count sizes
            }

        sorted_by_color[color]["items"].append(item)

        if size not in sorted_by_color[color]["size_counts"]:
            sorted_by_color[color]["size_counts"][size] = 0

        sorted_by_color[color]["size_counts"][size] += 1

    # Print the summary
    for color, data in sorted_by_color.items():
        # Start the summary line for the color
        summary = f"{color.capitalize()}: "
        # Append each size count to the summary line
        size_details = [f"{size} = {count}" for size, count in data["size_counts"].items()]
        # Join size details with commas
        summary += ", ".join(size_details)
        # Print the formatted summary line
        print(summary)


# Use the fastest sorting function to sort the delivery list
delivery_copy = delivery.copy()  # Ensure the original delivery list remains unchanged
sorted_delivery = fastest_sort_function(delivery_copy)  # Sort the copied list
sort_delivery(sorted_delivery)  # Summarize the sorted list
