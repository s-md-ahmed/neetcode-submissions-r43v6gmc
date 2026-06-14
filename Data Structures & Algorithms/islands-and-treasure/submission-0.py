from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        
        # 1. Initialize: Add all treasure chests to the queue
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # 2. Multi-source BFS: Spread from all treasures simultaneously
        while queue:
            r, c = queue.popleft()
            
            # Explore neighbors (Up, Down, Left, Right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))