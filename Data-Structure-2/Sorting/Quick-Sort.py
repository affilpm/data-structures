"""
🔹 Quick Sort (Divide and Conquer)
    • How it works: Picks a pivot, partitions the array into elements less than, equal to, 
      and greater than the pivot, then recursively sorts the partitions.
    • Time Complexity: 
        - Average: O(n log n)
        - Worst: O(n²) (rare, depends on pivot choice)
    • Best for: Large datasets, efficient in practice.
"""

# Quick sort using new arrays (not in-place)
def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.

    Args:
        arr (list): List of numbers to sort.
    
    Returns:
        list: Sorted list in ascending order.
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the pivot (here middle element)
        pivot = arr[len(arr)//2]

        # Partition the array into three lists
        left = [x for x in arr if x < pivot]      # Elements less than pivot
        middle = [x for x in arr if x == pivot]   # Elements equal to pivot
        right = [x for x in arr if x > pivot]     # Elements greater than pivot

        # Recursively sort left and right partitions and combine
        return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Sorted array:", quick_sort(arr))

      