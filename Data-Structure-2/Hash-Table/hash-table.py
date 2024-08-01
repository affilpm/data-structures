class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self,key):
        return hash(key) % self.size    
    
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i,v in enumerate(bucket):
            if v[0] == key:
                bucket[i] = (key,value)
                return
        bucket.append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return
            
              
    def display_all(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}") 
                
                
    def count(self,value):
        count = 0
        for bucket in self.table:
            for i,v in bucket:
                if v == value:
                    count += 1
            return count            
                               

ht = HashTable(10)
ht.insert("one", "2")
ht.insert("two", "35")
ht.insert("three", "35")
ht.insert("four", "35")
ht.insert("five", "35")
ht.insert("six", "35")
ht.delete("two")

ht.display_all()
# print(ht.search("key"))  
# print(ht.search("key")) 
    
        
        
    