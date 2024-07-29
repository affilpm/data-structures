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
    print('choose any one of the option 1.push 2.pop 3.display')
    choice = int(input())
    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    else:
        print('choose from any 3')            
        
   
        