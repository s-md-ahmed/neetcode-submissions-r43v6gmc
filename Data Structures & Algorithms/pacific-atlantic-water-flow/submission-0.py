from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Track reachability from each ocean
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(seeds, ocean):
            q = deque(seeds)
            for r, c in seeds:
                ocean[r][c] = True
                
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds, if already visited, and flow condition
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        ocean[nr][nc] = True
                        q.append((nr, nc))

        # Identify starting points for each ocean
        pacific_seeds = []
        atlantic_seeds = []
        for i in range(ROWS):
            pacific_seeds.append((i, 0))
            atlantic_seeds.append((i, COLS - 1))
        for j in range(COLS):
            pacific_seeds.append((0, j))
            atlantic_seeds.append((ROWS - 1, j))

        # Run BFS for both
        bfs(pacific_seeds, pac)
        bfs(atlantic_seeds, atl)

        # Collect common cells
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res