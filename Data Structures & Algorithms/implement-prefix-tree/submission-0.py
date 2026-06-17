'''
I hear you—you want to see the "mechanics" of how the data actually moves through the code, rather than just the abstract logic. Let's trace the exact function calls for `insert("do")` and `search("do")`.

### 1. Dry Run: `insert("do")`

When you call `insert("do")`, the `curr` pointer moves through the Trie nodes like a traveler.

1. **Call `insert("do")**`:
* `curr` starts at `root`.
* **Process 'd':** `'d'` is not in `root.children`.
* Create `TrieNode` for 'd'.
* `root.children['d'] = new_node_d`.
* `curr` moves to `new_node_d`.


* **Process 'o':** `'o'` is not in `new_node_d.children`.
* Create `TrieNode` for 'o'.
* `new_node_d.children['o'] = new_node_o`.
* `curr` moves to `new_node_o`.


* **Loop finishes.**
* `curr.isEndOfWord = True` (This flags `new_node_o`).



---

### 2. Dry Run: `search("do")`

Now, when you call `search("do")`, the code uses the exact same path to verify existence.

1. **Call `search("do")**`:
* `curr` starts at `root`.
* **Check 'd':** Is `'d'` in `root.children`? **Yes.**
* `curr` moves to `new_node_d`.


* **Check 'o':** Is `'o'` in `new_node_d.children`? **Yes.**
* `curr` moves to `new_node_o`.


* **Loop finishes.**
* **Return `curr.isEndOfWord**`: The function looks at `new_node_o` and sees `True`.
* **Result: `True`.**



---

### 3. Dry Run: `search("d")` (The "Why it fails" check)

This is where the function call makes the difference.

1. **Call `search("d")**`:
* `curr` starts at `root`.
* **Check 'd':** Is `'d'` in `root.children`? **Yes.**
* `curr` moves to `new_node_d`.


* **Loop finishes.**
* **Return `curr.isEndOfWord**`: The function looks at `new_node_d`.
* Did we ever set `isEndOfWord` to `True` for `'d'`? **No.** It is still the default `False`.


* **Result: `False`.**



### The "Joke" vs. The Reality

It's not a joke—the complexity of the Trie lies in the fact that it **strictly** obeys the `isEndOfWord` flag.

* If `insert("do")` was called, but `insert("d")` was **not**, the Trie simply does not recognize "d" as a valid word, even though the path for "d" exists.
* The `curr` pointer is just a way for the function to "walk" down the tree until it runs out of characters or hits a missing branch.

Does tracing the `curr` pointer's movement like a character-by-character "walk" make it feel less like magic and more like a systematic path-following process?
'''
class TrieNode:
    def __init__(self):
        # A dictionary to store children nodes: { 'char': TrieNode }
        self.children = {}
        
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True