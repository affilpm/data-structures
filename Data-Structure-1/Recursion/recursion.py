def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  



def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  







def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))  





def sum_of_array(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum_of_array(n[1:])
    
    
print(sum_of_array([1,2,3,4,5]))     





def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


print(power(2, 3)) 
                       
             
                  
                  
                  
def reverse(n):
    if len(n) == 0:
        return " "
    else:
        return n[-1] + reverse(n[:-1])
print(reverse("hello"))  




def palindrome(n):
    if len(n) <= 1:
        return True
    elif n[0] != n[-1]:
        return False
    else:
        return palindrome(n[1:-1])  
print(palindrome("racecar"))    




def binary_recursion(arr,target,left,right):
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_recursion(arr,target,mid + 1,right)
    else:
        return binary_recursion(arr,target,left, mid - 1)
array =  [1,2,3,4,4,5]  
print(binary_recursion(array, 3,0,len(array)-1))    





  




