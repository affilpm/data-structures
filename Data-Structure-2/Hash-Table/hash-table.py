class HashTable:
    def __init__(self, size):
        """
        Initialize the hash table with given size.
        Each slot contains a list to handle collisions (chaining).
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # List of empty buckets

    def hash_function(self, key):
        """
        Simple hash function using Python's built-in hash and modulo by table size.
        Returns the index where the key should be stored.
        """
        return hash(key) % self.size    

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If key already exists, update its value.
        """
        index = self.hash_function(key)       # Compute bucket index
        bucket = self.table[index]            # Get the bucket
        for i, v in enumerate(bucket):        # Check if key exists
            if v[0] == key:
                bucket[i] = (key, value)     # Update value if key exists
                return
        bucket.append((key, value))           # Otherwise, add new key-value pair

    def search(self, key):
        """
        Search for a key in the hash table.
        Returns the value if found, else None.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]                # Remove the key-value pair
                return
            
    def display_all(self):
        """
        Display all non-empty buckets and their contents.
        """
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}") 
                
    def count_duplicate_values(self, value):
        """
        Count how many times a particular value appears in the hash table.
        """
        count = 0
        for bucket in self.table:
            for i, v in bucket:
                if v == value:
                    count += 1
        return count             # Return total count


# Example usage
ht = HashTable(10)
ht.insert("one", "2")       # Insert key 'one' with value '2'
ht.insert("one", "0")       # Update key 'one' with value '0'
ht.insert("two", "35")      
ht.insert("three", "35")    
ht.insert("four", "35")     
ht.insert("five", "35")     
ht.insert("six", "35")      
ht.delete("two")            # Delete key 'two'

ht.display_all()            # Display non-empty buckets

# Searching for a key
# print(ht.search("key"))  
# print(ht.search("key")) 