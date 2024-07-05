def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
arr = [4, 2, 1, 5, 3]
print(linear_search(arr,3))






def linear_search2(array,target):
    for i in array:
        if i > target:
            return i
    return None
arr = [1,3,2,3,5,7]
print(linear_search2(arr,4))





def linear_search3(array,target):
    d=[]
    for i in range(len(array)):
        if array[i] == target:
            d.append(i)
    return d

arr = [1,3,2,3,5,7]
print(linear_search3(arr,3))
        
            
    
            