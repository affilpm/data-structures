class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self,key):
        return hash(key) % self.size    
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
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
ht.delete("two")

ht.display_all()
# print(ht.search("key"))  
# print(ht.search("key")) 
    
        
        
    