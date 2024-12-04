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
            
    def add_index(self,value,target):
        new_node = Node(value)
        if 0 == target:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        b = self.head
        c = 2
        
        while c < target:
            if b.next is not None:
                b = b.next
                c += 1
                
            else:
                print('target not found')
                return   
  
        if b is None:
            print('not found')
            return
        else:
            new_node.next = b.next
            new_node.prev = b
            if b.next:
                b.next.prev = new_node
            b.next = new_node
                        
                
                
                     
                                            
                
n = LinkedList()
# n.insert_empty(1)
n.add_begin(2)
n.add_begin(1)
# n.add_end(6)
n.add_after(3,1)
n.print_ll()    
n.print_ll_reverse()


#                     class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None  # Previous pointer


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     # Print doubly linked list
#     def print_LL(self):
#         if self.head is None:
#             print("LL is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, end=" <--> ")
#                 n = n.next
#         print()

#     # Adding new node at beginning
#     def add_begin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     # Adding new node at end
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.next is not None:
#                 n = n.next
#             n.next = new_node
#             new_node.prev = n

#     # Adding new node after a given node
#     def add_after(self, data, x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.next
#         if n is None:
#             print("Node you typed is not present in LL")
#         else:
#             new_node = Node(data)
#             new_node.next = n.next
#             new_node.prev = n
#             if n.next is not None:
#                 n.next.prev = new_node
#             n.next = new_node

#     # Adding new node before a given node
#     def add_before(self, data, x):
#         if self.head is None:
#             print("LL is empty")
#             return
#         if self.head.data == x:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#             return
#         n = self.head
#         while n.next is not None:
#             if n.next.data == x:
#                 break
#             n = n.next
#         if n.next is None:
#             print("Node is not found")
#         else:
#             new_node = Node(data)
#             new_node.next = n.next
#             new_node.prev = n
#             if n.next is not None:
#                 n.next.prev = new_node
#             n.next = new_node

#     # Adding new node in the middle
#     def add_mid(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         fast = self.head
#         slow = self.head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         new_node.next = slow.next
#         new_node.prev = slow
#         if slow.next is not None:
#             slow.next.prev = new_node
#         slow.next = new_node

#     # Delete node at the beginning
#     def del_begin(self):
#         if self.head is not None:
#             if self.head.next is not None:
#                 self.head.next.prev = None
#             self.head = self.head.next

#     # Delete node at the end
#     def del_end(self):
#         if self.head is None:
#             return
#         if self.head.next is None:
#             self.head = None
#             return
#         n = self.head
#         while n.next is not None:
#             n = n.next
#         n.prev.next = None

#     # Delete node after a given node
#     def del_after(self, x):
#         n = self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n = n.next
#         if n is None or n.next is None:
#             print("Node after the specified value is not found")
#         else:
#             n.next = n.next.next
#             if n.next is not None:
#                 n.next.prev = n

#     # Delete node in the middle
#     def del_mid(self):
#         if self.head is None or self.head.next is None:
#             print('Not enough nodes to delete from middle')
#             return
#         fast = self.head
#         slow = self.head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         if slow.prev is not None:
#             slow.prev.next = slow.next
#         if slow.next is not None:
#             slow.next.prev = slow.prev

#     # Delete node by value
#     def del_by_val(self, x):
#         if self.head is None:
#             print("LL is empty")
#             return
#         if self.head.data == x:
#             if self.head.next is not None:
#                 self.head.next.prev = None
#             self.head = self.head.next
#             return
#         n = self.head
#         while n is not None:
#             if n.data == x:
#                 break
#             n = n.next
#         if n is None:
#             print("Node is not present")
#         else:
#             if n.next is not None:
#                 n.next.prev = n.prev
#             if n.prev is not None:
#                 n.prev.next = n.next