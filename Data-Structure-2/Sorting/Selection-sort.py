# selection sort ascending order
def selection_sort1(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]       
    return arr

arr = [5,4,2,3,1,0]
print(selection_sort1(arr))    




# selection sort descending order
def selection_sort2(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] > arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr            
arr = [5,4,2,3,1,0]
print(selection_sort2(arr))           