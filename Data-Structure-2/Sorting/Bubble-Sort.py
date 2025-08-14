"""
🔹 Bubble Sort (Comparison-based Sorting)
    • How it works: Repeatedly compares adjacent elements and swaps them if they’re in the wrong order.
    • Time Complexity: O(n²)
    • Best for: Small or nearly sorted data.
"""

# ------------------------------
# Bubble sort in ascending order
# ------------------------------
def bubble_sort_ascending(arr):
    """
    Sorts the array in ascending order using bubble sort.
    
    Args:
        arr (list): List of numbers to be sorted.
        
    Returns:
        list: Sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3, 5, 6, 2, 4]
print("Ascending:", bubble_sort_ascending(arr))


# ------------------------------
# Bubble sort in descending order
# ------------------------------
def bubble_sort_descending(arr):
    """
    Sorts the array in descending order using bubble sort.
    
    Args:
        arr (list): List of numbers to be sorted.
        
    Returns:
        list: Sorted list in descending order.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if current element is smaller than next
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3, 5, 6, 2, 4]
print("Descending:", bubble_sort_descending(arr))