# stack working
class stack():
    def __init__(self) -> None:
        self.element = []
        
    def push(self):
        m = int(input('enter the element'))
        self.element.append(m)
        print(m,'added to list')
        
    def pop(self):
        if not self.element:
            print('stack is empty')
        else:    
            v = self.element.pop()
            print(v, 'popped from stack')
        
    def display(self):
        if not self.element:
            print('empty')
        else:    
            print(self.element)    
    
        
stack = stack()
while stack:
    print('choose any one of the option 1.push 2.pop 3.display 4.quit')
    choice = int(input())
    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        break
    else:
        print('choose from any 3') 
         
        
        
        
  
# Reverse stack
def reverse_stack(arr):
    reversed = []
    for i in range(len(arr)):
        reversed.append(arr.pop())
    return reversed
print(reverse_stack([1,2,3,4,5,6]))            
        
        
        
        
        
# Remove middle from stack          
def middle_stack(arr):
    mid = len(arr)//2
    d = []
    for i in range(mid):
        d.append(arr.pop())
    arr.pop()
    for j in range(len(d)):
        arr.append(d.pop())
    return arr
print(middle_stack([1,2,3,4,5]))    

 
   

        