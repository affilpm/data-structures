class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next
        print()
                
                
    def print_ll_reverse(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, end=' ')
                n = n.prev 
        print()
                
                
                
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('ll is not empty') 
            
            
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n               
            
               
    def add_after(self,data,x):
            if self.head is None:
                print('ll')
                return
            n = self.head    
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print('no node')
            else:
                new_node = Node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node   
                
                
                     
                                            
                
n = LinkedList()
# n.insert_empty(1)
n.add_begin(2)
n.add_begin(1)
# n.add_end(6)
n.add_after(3,1)
n.print_ll()    
n.print_ll_reverse()


                    