# Delivery Sorting

The Delivery Sorting project is a Python application that handles the classification and sorting of items based on color and size. It includes various sorting algorithms and a suite of tests to ensure the correctness and performance of these algorithms.

## Files Description

- `warehouse.py`: contains definitions for the sorting orders of colors and sizes
- `stock_room.py`: implements sorting algorithms and functions for managing stock items
- `script.py`: main script that uses the fastest sorting function to sort the items and prints a summary of the distribution
- `performance_analysis.py`: contains functions to analyze the performance of sorting algorithms
- `test_sort.py`: test suite to verify the correctness and performance of the code

## Requirements

- Python 3.7 or higher
- [pytest](https://docs.pytest.org/en/stable/) for running tests (included in `requirements.txt`)


## Installation and Execution
### Install

Clone the repository:
```bash
git clone https://github.com/m-grande/delivery-sorting.git
 ```
Navigate to the project directory:
```bash
cd delivery-sorting
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Run the Script

   To execute the main script, use the command:

   ```bash
   python3 sort/script.py
   ```

### Run Tests

To run the tests, use pytest:

```bash
pytest tests/test_sort.py
```

## How the Code Works

### warehouse.py
The **warehouse.py** file defines the data and structures used in the program:

`colors_order` and `sizes_order` map colors and sizes to integer values to facilitate comparison during sorting

`items_generator()` creates random items with color and size attributes

`delivery` is a list of randomly generated items, similar to a warehouse of items waiting to be sorted

### stock_room.py
The **stock_room.py** file contains implementations of three sorting algorithms:

`bubble_sort` sorts items by comparing them in pairs and swapping them if they are in the wrong order

`quick_sort` is an efficient sorting algorithm that uses the "divide and conquer" method to sort recursively

`merge_sort` divides the list into smaller sublists, sorts them separately, and then combines them to form a sorted list

### performance_analysis.py
The **performance_analysis.py** file manages the performance analysis of different sorting algorithms and determines which one is the fastest:

`measure_sort_time()` calculates the time taken by a sorting algorithm to sort a list of items

`get_fastest_sort_function()` evaluates the performance of three sorting algorithms: Bubble Sort, Quick Sort, and Merge Sort. After measuring the execution time of each, it selects and returns the fastest algorithm

### script.py
The **script.py** file serves as the entry point for the program. It uses the fastest sorting algorithm to sort a list of items and provides a summary of the results:

`sort_delivery()` creates a summary of the sorted items, organized by color and size, and prints it. The file uses the fastest sorting function determined by `performance_analysis.py` to sort a copy of the delivery list


### test_sort.py
The **test_sort.py** file contains unit tests to verify the correctness and functionality of the main components of the program:

`test_items_generator()` verifies that generated items have valid color and size attributes

`test_delivery_length()` and `test_delivery_content()` ensure that the delivery list has the correct length and contains valid items

`test_sorting_algorithms()` verifies that the sorting algorithms (Bubble Sort, Quick Sort, Merge Sort) correctly sort the list of items

`test_performance_analysis()` confirms that the `get_fastest_sort_function()` returns a valid sorting function and that it sorts the list correctly
