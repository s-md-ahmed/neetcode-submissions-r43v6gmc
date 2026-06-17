'''Let's trace the Union-Find logic on your input `[[1,2], [1,3], [3,4], [2,4]]`.

### Setup

We have 4 nodes, so we create a `parent` array of size 5 (indices 0 to 4):
`parent = [0, 1, 2, 3, 4]` (Initially, everyone is their own parent).

---

### Dry Run

1. **Edge `[1, 2]`:**
* `find(1)` is 1, `find(2)` is 2.
* Roots are different (1 ≠ 2).
* `union` merges them: `parent[1] = 2`.
* **New `parent`:** `[0, 2, 2, 3, 4]` (1 now points to 2).


2. **Edge `[1, 3]`:**
* `find(1)`: `parent[1]` is 2, `parent[2]` is 2. So root is 2.
* `find(3)` is 3.
* Roots are different (2 ≠ 3).
* `union` merges them: `parent[2] = 3`.
* **New `parent`:** `[0, 2, 3, 3, 4]` (1 points to 2, 2 points to 3).


3. **Edge `[3, 4]`:**
* `find(3)` is 3.
* `find(4)` is 4.
* Roots are different (3 ≠ 4).
* `union` merges them: `parent[3] = 4`.
* **New `parent`:** `[0, 2, 3, 4, 4]` (1->2, 2->3, 3->4).


4. **Edge `[2, 4]`:**
* `find(2)`: `parent[2]` is 3, `parent[3]` is 4, `parent[4]` is 4. So root is 4.
* `find(4)` is 4.
* **Roots are the same (4 == 4)!** * `union` returns `False`.
* **We found the cycle!** Return `[2, 4]`.



### Why this is the "trick":

Notice how `find` effectively collapsed the tree. By the time we hit the final edge `[2, 4]`, the `parent` array had essentially linked everything into one giant tree under root `4`. Since 2 and 4 already shared the same root, the algorithm knew instantly they were already connected—meaning that extra edge `[2, 4]` was the culprit.

Does this breakdown make the "merging" logic easier to visualize?'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = list(range(len(edges) + 1))#=[0,1,2,3,4] for Input: edges = [[1,2],[1,3],[3,4],[2,4]]

        
        def find(n):
            
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                
                return False
            
            parent[root1] = root2
            return True
            
        for n1, n2 in edges:
            if not union(n1, n2):
                
                return [n1, n2]