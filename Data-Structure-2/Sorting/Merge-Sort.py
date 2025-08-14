"""
🔹 Merge Sort (Divide and Conquer)
    • How it works: Divides the array into halves, sorts them, and merges the sorted halves.
    • Time Complexity: O(n log n)
    • Best for: Large datasets, stable sort.
"""

# ------------------------------
# In-place merge sort (simple version)
# ------------------------------
def merge_sort(arr):
    """
    Sorts an array in-place using merge sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]   # Left half
        R = arr[mid:]   # Right half

        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)

        # Merge sorted halves back into arr
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements, if any
        arr[k:] = L[i:] + R[j:]

arr = [4, 7, 3, 7, 4, 1, 35, 0]
merge_sort(arr)
print("Sorted array (in-place simple):", arr)


# ------------------------------
# In-place merge sort with separate merge function
# ------------------------------
def merge_sort(arr):
    """
    Sorts an array in-place using merge sort with a helper merge function.
    """
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    merge_sort(left)
    merge_sort(right)

    # Merge the sorted halves into original array
    merge(arr, left, right)

def merge(arr, left, right):
    """
    Merges two sorted arrays (left and right) into the original array arr.
    """
    i = j = k = 0

    # Merge elements from left and right in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array (in-place with merge):", arr)


# ------------------------------
# Merge sort using new array (returns new sorted array)
# ------------------------------
def merge_sort(arr):
    """
    Sorts an array using merge sort and returns a new sorted array.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a new sorted array.
    """
    sorted_arr = []
    i = j = 0

    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append remaining elements, if any
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

arr = [38, 27, 43, 4, 6, 7, 7]
print("Sorted array (new array version):", merge_sort(arr))