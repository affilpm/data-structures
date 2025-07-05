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