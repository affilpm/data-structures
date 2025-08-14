"""
🔹 Selection Sort (Comparison-based Sorting)
    • How it works: Repeatedly finds the minimum (or maximum) element from 
      the unsorted part and moves it to the beginning (or end).
    • Time Complexity: O(n²)
    • Best for: Simple scenarios with small datasets.
"""

# ------------------------------
# Selection sort in ascending order
# ------------------------------
def selection_sort1(arr):
    """
    Sorts the array in ascending order using selection sort.

    Args:
        arr (list): List of numbers to be sorted.
    
    Returns:
        list: Sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        min_ind = i  # Assume current index is the minimum
        # Find the actual minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

arr = [5, 4, 2, 3, 1, 0]
print("Ascending order:", selection_sort1(arr))


# ------------------------------
# Selection sort in descending order
# ------------------------------
def selection_sort2(arr):
    """
    Sorts the array in descending order using selection sort.

    Args:
        arr (list): List of numbers to be sorted.
    
    Returns:
        list: Sorted list in descending order.
    """
    n = len(arr)
    for i in range(n):
        max_ind = i  # Assume current index is the maximum
        # Find the actual maximum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] > arr[max_ind]:
                max_ind = j
        # Swap the found maximum element with the first unsorted element
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
    return arr

arr = [5, 4, 2, 3, 1, 0]
print("Descending order:", selection_sort2(arr))