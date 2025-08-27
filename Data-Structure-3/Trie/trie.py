# Define a class for each node in the Trie
class trienode():
    def __init__(self) -> None:
        self.child = {}             # Dictionary to store children nodes (character: trienode)
        self.endofword = False      # Boolean flag to mark the end of a complete word


# Define the main Trie class
class trie:
    def __init__(self) -> None:
        self.root = trienode()      # Initialize root node (empty node)

    # Insert a word into the Trie
    def insert(self, word):
        current = self.root         # Start from the root
        for i in word:
            if i not in current.child:
                current.child[i] = trienode()  # Create a new node if character not found
            current = current.child[i]        # Move to the child node
        current.endofword = True              # Mark the end of the word

    # Search for a complete word in the Trie
    def search(self, word):
        current = self.root
        for i in word:
            if i not in current.child:
                return False       # If any character not found, word doesn't exist
            current = current.child[i]
        return current.endofword   # Word exists only if endofword is True

    # Remove a word from the Trie (only marks it, doesn't delete nodes)
    def remove(self, word):
        current = self.root
        for i in word:
            if i not in current.child:
                return False       # Can't remove if word doesn't exist
            current = current.child[i]
        current.endofword = False  # Unmark the end of word
        # Note: This doesn't clean up unused nodes
        
    def delete(self, word):
        
        def _delete(current, word, depth):
            
            if current is None:
                return False
                
            if depth == len(word):
                if current.endofword == True:
                    current.endofword = False
                    return len(current.child) == 0 
                return False
                
            char = word[depth]
            
            if char in current.child:
                should_delete_child = _delete(current.child[char], word, depth + 1)
                if should_delete_child:
                    del current.child[char]
                    return len(current.child) == 0 and not current.endofword 
            return False
        _delete(self.root, word, 0)          

    # Check if there is any word in the Trie that starts with the given prefix
    def starts_with(self, prefix):
        current = self.root
        for i in prefix:
            if i not in current.child:
                return False
            current = current.child[i]
        return True                # If all characters found, prefix exists


# --------------------
# Example Usage
# --------------------

n = trie()
n.insert('affil')                  # Insert word 'affil'
print(n.search('affil'))          # True, word exists in trie

# print(n.starts_with('a'))       # Uncomment to check if any word starts with 'a'


# def list_all_words(self):
#     result = []
    
#     def dfs(node, path):
#         # If the node marks the end of a word, add it
#         if node.is_end_of_word:
#             result.append(path)
        
#         # Explore children
#         for char, child in node.children.items():
#             dfs(child, path + char)
    
#     dfs(self.root, "")
#     return result

# def autocomplete(self, prefix):
#     result = []
    
#     def dfs(node, path):
#         if node.is_end_of_word:
#             result.append(path)
#         for char, child in node.children.items():
#             dfs(child, path + char)
    
#     node = self.root
#     for char in prefix:
#         if char not in node.children:
#             return []  # No words with this prefix
#         node = node.children[char]
    
#     dfs(node, prefix)
#     return result

# def count_words_with_prefix(self, prefix):
#     def dfs_count(node):
#         count = 1 if node.is_end_of_word else 0
#         for child in node.children.values():
#             count += dfs_count(child)
#         return count
    
#     node = self.root
#     for char in prefix:
#         if char not in node.children:
#             return 0
#         node = node.children[char]
    
#     return dfs_count(node)