def binary_search(arr, target):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid-1
    return -1

h = [1,2,3,4,5,6]
print(binary_search(h,5))    




# find first occurence of target
def binary_search1(arr,target):
    left,right = 0, len(arr)-1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 2
    return result
print(binary_search1([1,1,1,2,3,4,4,5], 2))              
            





# find last occurrence of target
def binary_search2(arr, target):
    left,right = 0, len(arr)-1
    result = -1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result  
print(binary_search2([1,1,1,2,3,4,4,5], 1))




# replace target
def binary_search3(arr, target):
    left,right = 0,len(arr)-1
    n = []
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            arr[mid] = 0
            return arr
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid-1
    return -1

h = [1,2,3,4,5,6]
print(binary_search3(h,3))    





def doubly_recursion(arr,target,left,right):
    
    if len(arr) <= 1:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return doubly_recursion(arr,target,mid + 1,right)
    else:
        return doubly_recursion(arr,target,left, mid - 1)
array =  [1,2,3,4,4,5]  
print(doubly_recursion(array, 3,0,len(array)-1))    
