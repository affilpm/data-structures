#queue working
class queue():
    def __init__(self):
        self.arr = []
        
    def enqueue(self):
        element = int(input('enter value'))
        self.arr.append(element)
        print(element,'added to queue') 
        
    def dequeue(self):
        if not self.arr:
            print('queue is empty')
        else:    
            element = int(input('enter the object to remove'))       
            element = self.arr.pop(0)
            print(element, 'removed from queue')
        
    def display(self):
        if not self.arr:
            print('queue is empty')
        else:
            print(self.arr)
                      
queue = queue()        
while queue:
    print('choose a option 1.enqueue 2.dequeue 3.display 4.quit')
    choice = int(input())
    if choice == 1:
        queue.enqueue()
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:   
        break
    else:
        print('choose any of the mentioned options')
                                 
                                 
 
                                 
                                 
                                 
                                 

    
                                  