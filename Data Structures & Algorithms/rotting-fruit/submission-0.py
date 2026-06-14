from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # 1. Initialize: Find all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If no fresh oranges to start with, return 0
        if fresh_count == 0:
            return 0
            
        minutes = 0
        # Directions for 4-way movement
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Start the rotting process
        while queue and fresh_count > 0:
            minutes += 1
            # Process only the oranges that were rotten at the start of this minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If the neighbor is a fresh orange, it becomes rotten
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        # 3. Final Result
        return minutes if fresh_count == 0 else -1