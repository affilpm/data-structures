# 🔡 Trie (Prefix Tree) Data Structure

This directory contains a simple yet powerful implementation of a **Trie** (also known as a **Prefix Tree**) in Python.

A Trie is an efficient information retrieval data structure that is especially useful for handling dynamic sets of strings such as dictionaries, autocomplete systems, and spell checkers.

---

## 📁 File Structure

- `trie.py` – Contains the full implementation of the `TrieNode` and `Trie` classes.
- Example usage is provided at the bottom of the file for quick testing.

---

## 🚀 Features

- ✅ Insert words into the Trie
- 🔍 Search for complete words
- ❌ Remove a word (logical removal)
- 🔤 Check if any word starts with a given prefix

---

## 🧱 Trie Structure Overview

Each Trie node contains:
- `child`: A dictionary of children nodes mapping characters to `TrieNode`
- `endofword`: A boolean flag to indicate whether a word ends at this node

**Visual Example:**

Inserting `["app", "apple", "bat"]` creates the following structure:

                 root
                /    \
               a      b
              /        \
             p          a
            /            \
           p(end)        t(end)
          /  
         e(end)


---

## ⚙️ How It Works

### `insert(word)`
Traverses each character:
- If it doesn’t exist in the current node’s children, creates a new `TrieNode`.
- Marks the final node’s `endofword = True`.

### `search(word)`
- Checks if all characters exist and if the last node is marked as `endofword`.

### `starts_with(prefix)`
- Same as search but doesn't require the last node to be an end of a word.

### `remove(word)`
- Traverses like search.
- If found, unmarks the `endofword = False`. *(Doesn't delete nodes for simplicity.)*

---

## 🧠 Time and Space Complexity

| Operation      | Time Complexity | Space Complexity |
|----------------|------------------|------------------|
| Insert         | O(L)             | O(L)             |
| Search         | O(L)             | O(1)             |
| Starts With    | O(L)             | O(1)             |

Where `L` is the length of the input word or prefix.

---

## ✅ Usage Example

```python
from trie import trie

t = trie()
t.insert("apple")
print(t.search("apple"))   # True
print(t.search("app"))     # False
print(t.starts_with("app"))# True
t.insert("app")
print(t.search("app"))     # True
t.remove("app")
print(t.search("app"))     # False        

## 📌 To Do

- [ ] Implement **physical deletion** of unused nodes on removal  
- [ ] Add **autocomplete functionality** using DFS  
- [ ] Add support for **case-insensitive** insert/search  

---

## 👨‍💻 Author

**AFFIL P M**  
GitHub: [@affilpm](https://github.com/affilpm)

---