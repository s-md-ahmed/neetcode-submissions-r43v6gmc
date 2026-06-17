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