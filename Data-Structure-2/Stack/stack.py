stack = []
def push():
    if len(stack) == limit:
        print("stack is full")
    else:    
        element = int(input("Enter the element:"))
        stack.append(element)
        print(element, 'added to the stack')
    
    
def pop():
    if not stack:
        print('Stack is empty')
    else:
        element = stack.pop()
        print("removed element", element)
        
def display():
    if not stack:
        print('Stack is empty')
    else:
        print(stack)            
            
limit = int(input('enter limit of stack:')) 
print(limit) 

while True:
    print('select the operation 1.push 2.pop 3.display 4.quit')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break    
    else:
        print('enter the correct operation')
            
        

          