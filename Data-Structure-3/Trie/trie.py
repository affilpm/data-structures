class trienode():
    def __init__(self) -> None:
        self.child = {}
        self.endofword = False
        
class trie:
    def __init__(self) -> None:
        self.root = trienode()
        
    def insert(self,word):
        current = self.root
        for i in word:
            if i not in current.child:
                current.child[i] = trienode()
            current = current.child[i]
        current.endofword = True
        
                
    def search(self, word):
        current = self.root
        for i in word:
            if i not in current.child:
                return False
            current = current.child[i]
        return current.endofword
    
    def starts_with(self,prefix):
        current = self.root
        for i in prefix:
            if i not in current.child:
                return False
            current = current.child[i]
        return True    
    
n = trie()
n.insert('affil')
print(n.search('affi'))                    
print(n.starts_with('a'))