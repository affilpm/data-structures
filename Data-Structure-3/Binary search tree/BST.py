class node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class bst:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,value):
        new_node = node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif value == current.value:
                return
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
                
    def contains(self,value):
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False
    
    def get_min(current):
        while current is not None:
            current = current.left
        return current    
        
    def delete(self,value):
        result = []
        def remove(current,value):
            if current is None:
                return current
            if value < current.value:
                current = remove(current.left, value)
            elif value > current.value:
                current = remove(current.right, value)
            else:
                if current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                min_val_right = self.get_min(current.right)
                current.value = min_val_right.value
                current.right = remove(current.right,value)
            return current
        self.root = remove(self.root, value)
        
        
    def is_bst(self, current = None, left = float('-inf'), right = float("inf")):
        if current is None:
            return True
        if not left < current.value < right:
            return False
        return (self.is_bst(current.left, left, current.value) and self.is_bst(current.right, right, current.value))
     
    
    def pre_order(self):
        result = []
        def traverse(current):
            if current is not None:
                result.append(current.value)
                traverse(current.left)
                traverse(current.right)
            return
        traverse(self.root)
        return result       
        
    
    def in_order(self):
        result = []
        def traverse(current):
            if current is not None:
                traverse(current.left)
                result.append(current.value)
                traverse(current.right)
            return
        traverse(self.root)
        return result    
    
    
    
    def post_order(self):
        result = []
        def traverse(current):
            if current is not None:
                traverse(current.left)
                traverse(current.right)
                result.append(current.value)

            return
        traverse(self.root)
        return result   
    
                 
n = bst()
n.insert(7)
# n.delete(7)
print(n.is_bst())
print(n.post_order())
print(n.contains(7)) 