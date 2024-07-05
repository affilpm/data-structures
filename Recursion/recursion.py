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






def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Example usage:
print(power(2, 3))  # Output: 8
                       
             
                  
                  
                  
                  
                  
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))





def summ(n):
    if n == 0:
        return 0
    else:
        return n % 10 + summ(n//10)    
print(summ(13411)) 




def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
    
print(power(2,3))       




