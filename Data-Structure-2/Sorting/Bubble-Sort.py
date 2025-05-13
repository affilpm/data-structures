# bubble sort in ascending order
def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n - i -1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [3,5,6,2,4]
print(bubble_sort1(arr))



# bubble sort in descending order
def bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr            
arr = [3,5,6,2,4]
print(bubble_sort2(arr))
            
            