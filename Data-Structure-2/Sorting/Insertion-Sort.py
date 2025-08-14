"""
🔹 Insertion Sort (Comparison-based Sorting)
    • How it works: Builds the sorted array one element at a time by inserting 
      each element into its correct position.
    • Time Complexity: O(n²)
    • Best for: Small datasets or nearly sorted data.
"""

# ------------------------------
# Insertion sort function
# ------------------------------
def insertion_sort(arr):
    """
    Sorts the array in ascending order using insertion sort.
    
    Args:
        arr (list): List of numbers to be sorted.
        
    Returns:
        list: Sorted list in ascending order.
    """
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key at correct position
    return arr

arr = [0, 2, 6, 3, 4, 5, 1]
print("Sorted array:", insertion_sort(arr))