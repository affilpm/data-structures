class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def delete(self, key):
        if not self.head:
            print("List is empty")
            return
        
        # Deleting head node
        if self.head.data == key:
            if self.head.next == self.head:  # Only one node
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return
        
        # Deleting other nodes
        prev = None
        temp = self.head
        while temp.next != self.head and temp.data != key:
            prev = temp
            temp = temp.next

        if temp.data == key:
            prev.next = temp.next
        else:
            print("Key not found in the list")

# Example usage:
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()  # Output: 10 -> 20 -> 30 ->
cll.delete(20)
cll.display()  # Output: 10 -> 30 ->