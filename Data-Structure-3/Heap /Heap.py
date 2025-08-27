class MaxHeap:
    def __init__(self):
        # Use a list to store heap elements
        self.heap = []

    # --------------------
    # Helper functions
    # --------------------
    def parent(self, i): 
        return (i - 1) // 2   # Parent index

    def left(self, i): 
        return 2 * i + 1      # Left child index

    def right(self, i): 
        return 2 * i + 2      # Right child index

    # --------------------
    # Insert new value
    # --------------------
    def insert(self, value):
        # Step 1: Add value at the end of heap
        self.heap.append(value)

        # Step 2: Heapify upwards (fix heap property)
        self.heapify_up(len(self.heap) - 1)

    # --------------------
    # Extract max (root element)
    # --------------------
    def extract_max(self):
        if not self.heap:
            return None   # Empty heap → return None

        if len(self.heap) == 1:
            return self.heap.pop()   # Only one element

        # Step 1: Save root (max value)
        root = self.heap[0]

        # Step 2: Move last element to root
        self.heap[0] = self.heap.pop()

        # Step 3: Heapify down to fix heap property
        self.heapify_down(0)

        return root

    # --------------------
    # Delete element at index i
    # --------------------
    def delete(self, i):
        if i >= len(self.heap):
            return None   # Index out of range

        # Step 1: Save value to be deleted
        deleted_value = self.heap[i]

        # Step 2: Take last element
        last_value = self.heap.pop()

        # Step 3: If we didn’t just remove the last element,
        # replace the deleted spot with last_value
        if i < len(self.heap):
            self.heap[i] = last_value

            # Step 4: Fix heap property
            # If new value is bigger than parent → move up
            if i > 0 and self.heap[i] > self.heap[self.parent(i)]:
                self.heapify_up(i)
            else:
                # Otherwise → move down
                self.heapify_down(i)

        return deleted_value

    # --------------------
    # Heapify Up (fix when inserting or moving up)
    # --------------------
    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            # Swap with parent if bigger
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)  # Move up

    # --------------------
    # Heapify Down (fix when extracting or moving down)
    # --------------------
    def heapify_down(self, i):
        largest = i
        left, right = self.left(i), self.right(i)

        # Check if left child is bigger
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child is bigger
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If either child is bigger → swap and continue
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)

    # --------------------
    # Peek root element (max value)
    # --------------------
    def peek(self):
        return self.heap[0] if self.heap else None
    
    
    
    
    
    
class MinHeap:
    def __init__(self):
        # Use a list to store heap elements
        self.heap = []

    # --------------------
    # Helper functions
    # --------------------
    def parent(self, i): 
        return (i - 1) // 2   # Parent index

    def left(self, i): 
        return 2 * i + 1      # Left child index

    def right(self, i): 
        return 2 * i + 2      # Right child index

    # --------------------
    # Insert new value
    # --------------------
    def insert(self, value):
        # Step 1: Add value at the end
        self.heap.append(value)

        # Step 2: Heapify upwards (fix heap property)
        self.heapify_up(len(self.heap) - 1)

    # --------------------
    # Extract min (root element)
    # --------------------
    def extract_min(self):
        if not self.heap:
            return None   # Empty heap → return None

        if len(self.heap) == 1:
            return self.heap.pop()   # Only one element

        # Step 1: Save root (min value)
        root = self.heap[0]

        # Step 2: Move last element to root
        self.heap[0] = self.heap.pop()

        # Step 3: Heapify down to restore heap property
        self.heapify_down(0)

        return root

    # --------------------
    # Delete element at index i
    # --------------------
    def delete(self, i):
        if i >= len(self.heap):
            return None   # Index out of range

        # Step 1: Save value to be deleted
        deleted_value = self.heap[i]

        # Step 2: Take last element
        last_value = self.heap.pop()

        # Step 3: If we didn’t just remove the last element,
        # replace the deleted spot with last_value
        if i < len(self.heap):
            self.heap[i] = last_value

            # Step 4: Fix heap property
            # If new value is smaller than parent → move up
            if i > 0 and self.heap[i] < self.heap[self.parent(i)]:
                self.heapify_up(i)
            else:
                # Otherwise → move down
                self.heapify_down(i)

        return deleted_value

    # --------------------
    # Heapify Up (fix when inserting or moving up)
    # --------------------
    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            # Swap with parent if smaller
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)  # Move up

    # --------------------
    # Heapify Down (fix when extracting or moving down)
    # --------------------
    def heapify_down(self, i):
        smallest = i
        left, right = self.left(i), self.right(i)

        # Check if left child is smaller
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if right child is smaller
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If any child is smaller → swap and continue
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    # --------------------
    # Peek root element (min value)
    # --------------------
    def peek(self):
        return self.heap[0] if self.heap else None    