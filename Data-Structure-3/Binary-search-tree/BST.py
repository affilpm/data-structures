# -------------------------------
# Node class: Represents a single node in the Binary Search Tree
# -------------------------------
class Node:
    def __init__(self, value) -> None:
        # The value stored in the node
        self.value = value
        
        # Left child pointer (will point to another Node or None)
        # All values smaller than 'value' will go to the left subtree
        self.left = None
        
        # Right child pointer (will point to another Node or None)
        # All values greater than 'value' will go to the right subtree
        self.right = None
        

# -------------------------------
# BST class: Represents the Binary Search Tree and its operations
# -------------------------------
class BST:
    def __init__(self) -> None:
        # Initially, the tree has no nodes, so root is None
        self.root = None
        
    # ---------------------------
    # INSERT: Add a new value into the BST
    # ---------------------------
    def insert(self, value):
        new_node = Node(value)  # Create a new node with the given value
        
        # If the tree is empty, this node becomes the root
        if self.root is None:
            self.root = new_node
            return
        
        # If the tree already has nodes, find the correct position for insertion
        current = self.root
        while True:
            if value < current.value:
                # Go to left side
                if current.left is None:
                    current.left = new_node  # Found an empty spot
                    return
                current = current.left     # Move further left
            elif value == current.value:
                # We do not allow duplicates in BST (can be changed if needed)
                return
            else:
                # Go to right side
                if current.right is None:
                    current.right = new_node  # Found an empty spot
                    return
                current = current.right      # Move further right
                
    # ---------------------------
    # CONTAINS: Search for a value in the BST
    # ---------------------------
    def contains(self, value):
        current = self.root  # Start from the root
        while current:
            if value < current.value:
                # If the value is smaller, go left
                current = current.left
            elif value > current.value:
                # If the value is bigger, go right
                current = current.right
            else:
                # If equal, value found
                return True
        # If loop ends, value not found
        return False
    
    # ---------------------------
    # GET MINIMUM NODE: Helper to find smallest value in a subtree
    # ---------------------------
    def get_min(self, current):
        # Keep going left until there are no more left children
        while current.left:
            current = current.left
        return current    
        
    # ---------------------------
    # DELETE: Remove a node from the BST
    # ---------------------------
    def delete(self, value):

        # Recursive helper function to remove a node
        def remove(current, value):
            # Base case: empty subtree
            if current is None:
                return current
            
            if value < current.value:
                # Search in the left subtree
                current = remove(current.left, value)
            elif value > current.value:
                # Search in the right subtree
                current = remove(current.right, value)
            else:
                # FOUND the node to delete
                
                # Case 1: Node has no left child
                if current.left is None:
                    return current.right  # Replace with right child
                
                # Case 2: Node has no right child
                elif current.right is None:
                    return current.left   # Replace with left child
                
                # Case 3: Node has two children
                # Find the smallest value in the right subtree
                min_val_right = self.get_min(current.right)
                current.value = min_val_right.value  # Replace value
                
                # Delete the duplicate from the right subtree
                current.right = remove(current.right, value)
            
            return current
        
        # Start deletion from the root
        self.root = remove(self.root, value)
        
    # ---------------------------
    # IS_BST: Check if the tree satisfies BST property
    # ---------------------------
    def is_bst(self, current=None, left=float('-inf'), right=float("inf")):
        # If reached an empty node, return True
        if current is None:
            return True
        
        # If value is not within valid range, it's not a BST
        if not left < current.value < right:
            return False
        
        # Recursively check left and right subtrees
        return (self.is_bst(current.left, left, current.value) and 
                self.is_bst(current.right, current.value, right))
     
    # ---------------------------
    # PRE-ORDER TRAVERSAL: Root → Left → Right
    # ---------------------------
    def pre_order(self):
        result = []
        
        def traverse(current):
            if current is not None:
                result.append(current.value)  # Visit root
                traverse(current.left)        # Visit left subtree
                traverse(current.right)       # Visit right subtree
            return
        
        traverse(self.root)
        return result       
       
    # ---------------------------
    # IN-ORDER TRAVERSAL: Left → Root → Right
    # This traversal gives sorted order for BST
    # ---------------------------
    def in_order(self):
        result = []
        
        def traverse(current):
            if current is not None:
                traverse(current.left)        # Visit left subtree
                result.append(current.value)  # Visit root
                traverse(current.right)       # Visit right subtree
            return
        
        traverse(self.root)
        return result    
    
    # ---------------------------
    # POST-ORDER TRAVERSAL: Left → Right → Root
    # ---------------------------
    def post_order(self):
        result = []
        
        def traverse(current):
            if current is not None:
                traverse(current.left)        # Visit left subtree
                traverse(current.right)       # Visit right subtree
                result.append(current.value)  # Visit root
            return
        
        traverse(self.root)
        return result   
    
                 
# -------------------------------
# Example usage of BST
# -------------------------------
n = BST()
n.insert(7)                 # Insert a single value into tree
# n.delete(7)               # Uncomment to test deletion

print(n.is_bst())           # Check if the tree is a valid BST
print(n.post_order())       # Display post-order traversal
print(n.contains(7))        # Search for value 7