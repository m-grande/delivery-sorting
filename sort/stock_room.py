import random

from .warehouse import colors_order, sizes_order


def bubble_sort(items):

    # Perform Bubble Sort
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare first by color
            if colors_order[items[j]["color"]] > colors_order[items[j + 1]["color"]]:
                items[j], items[j + 1] = items[j + 1], items[j]
            # If colors are the same, compare by size
            elif (
                colors_order[items[j]["color"]] == colors_order[items[j + 1]["color"]]
                and sizes_order[items[j]["size"]] > sizes_order[items[j + 1]["size"]]
            ):
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def quick_sort(items):
    # Helper function to compare two items
    def compare(item1, item2):
        if colors_order[item1["color"]] < colors_order[item2["color"]]:
            return True
        elif colors_order[item1["color"]] == colors_order[item2["color"]]:
            return sizes_order[item1["size"]] < sizes_order[item2["size"]]
        else:
            return False

    # Partition function for in-place sorting
    def partition(items, low, high):
        pivot_index = random.randint(low, high)
        pivot = items[pivot_index]
        items[pivot_index], items[high] = items[high], items[pivot_index]
        i = low

        for j in range(low, high):
            if compare(items[j], pivot):
                items[i], items[j] = items[j], items[i]
                i += 1

        items[i], items[high] = items[high], items[i]
        return i

    # Recursive quicksort function with in-place partitioning
    def sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            sort(items, low, pivot_index - 1)
            sort(items, pivot_index + 1, high)

    sort(items, 0, len(items) - 1)
    return items


def merge_sort(items):
    # Helper function to compare two items
    def compare(item1, item2):
        if colors_order[item1["color"]] < colors_order[item2["color"]]:
            return -1
        elif colors_order[item1["color"]] > colors_order[item2["color"]]:
            return 1
        else:
            if sizes_order[item1["size"]] < sizes_order[item2["size"]]:
                return -1
            elif sizes_order[item1["size"]] > sizes_order[item2["size"]]:
                return 1
            else:
                return 0

    # Merge function
    def merge(left, right):
        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if compare(left[left_index], right[right_index]) <= 0:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        # Append remaining elements
        if left_index < len(left):
            result.extend(left[left_index:])
        if right_index < len(right):
            result.extend(right[right_index:])

        return result

    # Merge Sort function
    def sort(items):
        if len(items) <= 1:
            return items
        middle_index = len(items) // 2
        left_split = items[:middle_index]
        right_split = items[middle_index:]

        left_sorted = sort(left_split)
        right_sorted = sort(right_split)

        return merge(left_sorted, right_sorted)

    return sort(items)
