class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
      
        
class Linkedlist():
    def __init__(self):
        self.head = None
        
        
        
# print linked list        
    def print_LL(self):
        if self.head is None:
            print("LL is empty",)
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.next



#adding new node at beginning 
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head     
        self.head = new_node
        
        
        

#adding new node at end     
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node  
            
          
              
# adding new after a node                                 
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.next
        if n is None:
            print("Node you typed is not present in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node      
            


# adding new node before a node
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data==x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            
            
            

# adding new node in the middle  
    def add_mid(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        fast = self.head
        slow = self.head
        prev = self.head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        if prev is not None:
            new_node.next = prev.next
            prev.next = new_node   
        else:
            new_node.next = self.head
            self.head = new_node                       







# delete node at the beginning            
    def del_begin(self):
        if self.head is not None:
            self.head = self.head.next 
            
            
# delete node at the end           
    def del_end(self):
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None
        
     
# del after a node
    def del_after(self,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print('no node you typed exist')
        elif n.next is None:
            print('no node', x)    
        else:
            n.next = n.next.next            


# delete node in the middle
    def del_mid(self):
        if self.head is None or self.head.next is None:
            print('not have enough node for deleting from middle')
            return
        fast = self.head
        slow = self.head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        if prev:
            prev.next = slow.next
            
            
            
                
# delete node by searching value        
    def del_by_val(self,x):
        if self.head is None:
            print("Ll is empty")
            return
        if x==self.head.next.data:
            self.head = self.head.next
            return 
        n = self.head
        while n.next is not None:
              if x==n.next.data:
                  break
              n = n.next
        if n.next is None:
            print("nod is not present")
        else:
            n.next = n.next.next    
            
         
    
              
   
        
# remove duplicate node       
    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
            
            
            
            
        
# reverse linked list    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev    
      
            
            
                     
                
# convert array to linked list            
def array_to_linked_list(arr):
    linked_list = Linkedlist()
    for item in arr:
        linked_list.add_end(item)
    return linked_list





# arr = [1, 3, 4, 5]
# linked_list = array_to_linked_list(arr)
# linked_list.print_LL()

LL1 = Linkedlist()

LL1.add_begin(1)
LL1.add_begin(10)
LL1.add_begin(6)
LL1.del_after(6)

# LL1.add_begin(7)
# LL1.add_end(6)     
# LL1.add_after(9,1)
# LL1.add_mid(4)
# LL1.add_begin(10)
# LL1.add_begin(10)
# LL1.del_end()
# LL1.del_begin()
# LL1.add_before(3,1)
# LL1.del_by_val(1)
# LL1.remove_duplicates()
# LL1.del_after()


# LL1.reverse()


LL1.print_LL()        
            






