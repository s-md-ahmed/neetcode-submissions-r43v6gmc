from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        
        clones = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                
                clones[curr].neighbors.append(clones[neighbor])
                
        
        return clones[node]