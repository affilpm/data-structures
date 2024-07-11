def p(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0:
            return False
    return True
n = [1,2,3,4,5,6,7]
for i in n:
    if p(i):
        print(f'{i} is prime') 
    else:
        print('not prime')       
        
        
        
       


def febonacci(n):
    f = [0,1]
    for i in range(2, n):
        f.append(f[-1]+ f[-2])
    return f
print(febonacci(6))    






def factorial(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d
print(factorial(5))    





def palindrome(n):
    b = n.lower()
    return b == b[::-1]
n = 'racecar'
print(palindrome(n))





def swap(r):
    n = list(r)
    n[2],n[3] = n[3],n[2]
    return ''.join(n)
n = 'goodboy'
print(swap(n))   





def reverse(d):
    return d[::-1]
d = 'car'
print(reverse(d)) 
    



def anagram(str1,str2):
    return sorted(str1) == sorted(str2)
print(anagram('list','tsil'))




def largest_number(n):
    largest_num = 0
    for i in n:
        if i > largest_num:
            largest_num = i
    return largest_num
print(largest_number([1,2,7,4,6,5])) 



def second_largest_number(n):
    largest_num = 0
    second_largest_num = 0
    for i in n:
        if i > largest_num:
            second_largest_num = largest_num
            largest_num = i
        elif i > second_largest_num and i != largest_num:
            second_largest_num = i    
    return second_largest_num
print(second_largest_number([1,2,7,4,6,5])) 



# print duplicates
def duplicates(n):
    seen = []
    duplicate = []
    for i in n:
        if i in seen:
            duplicate.append(i)
        else:
            seen.append(i)
    return duplicate
print(duplicates([1,2,7,3,2,5,4,6,5])) 



# remove duplicates in a list
def remove_duplicates(n):
    seen = []
    new_list = []
    for i in n:
        if i not in seen:
            seen.append(i)
            new_list.append(i)
    return new_list
print(remove_duplicates([1,2,7,2,3,2,5,4,6,5])) 




# remove duplicates in a str
def remove_duplicates_str(n):
    seen = ""
    new_str = ""
    m = n.split()
    for i in m:
        if i not in seen:
            seen += i + ","
            new_str += i + ","
    return new_str   
print(remove_duplicates_str("1,2,7,2,3,2,5,4,6,5"))     




 
# most occuring number
def largest_frequency(n):
    freq = {}
    for i in n:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    object_max_freq = None
    max_freq = 0
    for v,f in freq.items():
        if f > max_freq:
            max_freq = f
            object_max_freq = v
    return object_max_freq
v = [1,2,3,2,3,4,5,3]  
print(largest_frequency(v))      
            
                   


# reverse list without slicing
def reverse_arr(n):
    b = []
    for i in range(len(n)-1,-1,-1):
        b.append(n[i])
    return b
arr = [1,2,3,4,5]
print(reverse_arr(arr))    