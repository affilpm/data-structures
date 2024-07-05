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
        
        
        
       


def feb(n):
    f = [0,1]
    for i in range(2, n):
        f.append(f[-1]+ f[-2])
    return f
print(feb(6))    






def fac(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d
print(fac(5))    





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
    


