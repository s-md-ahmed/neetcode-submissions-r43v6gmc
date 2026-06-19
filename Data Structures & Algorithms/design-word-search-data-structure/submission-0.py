'''
To give you a proper "under-the-hood" look, let's dry run `search(".ay")` with a populated Trie.

### The Setup

Imagine we have already called:

* `addWord("day")`
* `addWord("bay")`
* `addWord("may")`

Your Trie structure now looks like this:

---

### The Dry Run: `search(".ay")`

**Initialization:**
`current_nodes = [root]`

#### Step 1: Process `char = '.'`

* We look at `current_nodes` (which is `[root]`).
* Since it's a `.`, we take **all** children of `root`.
* `next_nodes` becomes: `[Node('d'), Node('b'), Node('m')]`.
* `current_nodes` is now `[Node('d'), Node('b'), Node('m')]`.

#### Step 2: Process `char = 'a'`

* We look at each node in `current_nodes`:
* Does `Node('d')` have an `'a'`? **Yes**, move to `Node('a')` (the one after 'd').
* Does `Node('b')` have an `'a'`? **Yes**, move to `Node('a')` (the one after 'b').
* Does `Node('m')` have an `'a'`? **Yes**, move to `Node('a')` (the one after 'm').


* `next_nodes` becomes: `[Node('a_from_d'), Node('a_from_b'), Node('a_from_m')]`.
* `current_nodes` is updated.

#### Step 3: Process `char = 'y'`

* We look at each node in `current_nodes`:
* Does `Node('a_from_d')` have a `'y'`? **Yes**, move to `Node('y')`.
* Does `Node('a_from_b')` have a `'y'`? **Yes**, move to `Node('y')`.
* Does `Node('a_from_m')` have a `'y'`? **Yes**, move to `Node('y')`.


* `next_nodes` becomes: `[Node('y_from_day'), Node('y_from_bay'), Node('y_from_may')]`.
* `current_nodes` is updated.

#### Final Step: The `any()` check

* We look at our `current_nodes` list: `[Node('y_from_day'), Node('y_from_bay'), Node('y_from_may')]`.
* We check: `isEndOfWord` for each of these.
* All three are `True` because "day", "bay", and "may" were inserted.
* **Result:** `any(...)` returns `True`.
'''
class TrieNode:
    def __init__(self):
        
        self.children = {}
        
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        current_nodes = [self.root]
        
        for char in word:
            next_nodes = []
            for node in current_nodes:
                if char == '.':
                    
                    next_nodes.extend(node.children.values())
                elif char in node.children:
                    
                    next_nodes.append(node.children[char])
            
            
            if not next_nodes:
                return False
            current_nodes = next_nodes
            
        
        return any(node.isEndOfWord for node in current_nodes)