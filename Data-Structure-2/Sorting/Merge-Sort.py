# In-Place Merge Sort
def merge_sort(arr):
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    return merge(arr, left,right)

def merge(arr,left,right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr

print(merge_sort([3,4,5,7,1,2,9,0]))     










# merge sort using new array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    sorted_arr = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j]) 
            j += 1  
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr         

arr = [38, 27, 43,4,6,7,7]
print("Sorted array:", merge_sort(arr))
    