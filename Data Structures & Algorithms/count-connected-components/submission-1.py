class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        count = n
        
        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]
        
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            
            if root_u != root_v:
                parent[root_u] = root_v
                count -= 1
                
        return count