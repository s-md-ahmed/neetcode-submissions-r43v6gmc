import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        DETAILED STEP-BY-STEP DRY RUN
        
        Input Grid (2x2):
        [0, 3]
        [2, 4]
        
        Initialization:
        - N = 2
        - min_heap = [(0, 0, 0)]  -> format: (time/max_height, row, col)
        - visited  = {(0, 0)}
        
        ------------------------------------------------------------------------
        ITERATION 1:
        ------------------------------------------------------------------------
        1. Pop from min_heap: t=0, r=0, c=0 (Value: 0)
        2. Check target: Is (0, 0) == (1, 1)? No.
        3. Explore Neighbors of (0,0):
           
           ● Down Neighbor: (1, 0) -> Value is 2
             - Not visited. Add to visited: {(0,0), (1,0)}
             - Calculate cost: max(t, grid[1][0]) = max(0, 2) = 2
             - Push to heap: (2, 1, 0)
             
           ● Right Neighbor: (0, 1) -> Value is 3
             - Not visited. Add to visited: {(0,0), (1,0), (0,1)}
             - Calculate cost: max(t, grid[0][1]) = max(0, 3) = 3
             - Push to heap: (3, 0, 1)
             
        Current min_heap state: [(2, 1, 0), (3, 0, 1)]

        ------------------------------------------------------------------------
        ITERATION 2:
        ------------------------------------------------------------------------
        1. Pop from min_heap: t=2, r=1, c=0 (Value: 2) -> Min-heap chooses 2 over 3!
        2. Check target: Is (1, 0) == (1, 1)? No.
        3. Explore Neighbors of (1,0):
           
           ● Up Neighbor: (0, 0) -> Already visited. Skip.
           
           ● Right Neighbor: (1, 1) -> Value is 4
             - Not visited. Add to visited: {(0,0), (1,0), (0,1), (1,1)}
             - Calculate cost: max(t, grid[1][1]) = max(2, 4) = 4
             - Push to heap: (4, 1, 1)
             
        Current min_heap state: [(3, 0, 1), (4, 1, 1)]

        ------------------------------------------------------------------------
        ITERATION 3:
        ------------------------------------------------------------------------
        1. Pop from min_heap: t=3, r=0, c=1 (Value: 3)
        2. Check target: Is (0, 1) == (1, 1)? No.
        3. Explore Neighbors of (0,1):
           - Left (0,0) and Down (1,1) are both already in 'visited'. Skip.
           
        Current min_heap state: [(4, 1, 1)]

        ------------------------------------------------------------------------
        ITERATION 4:
        ------------------------------------------------------------------------
        1. Pop from min_heap: t=4, r=1, c=1 (Value: 4)
        2. Check target: Is (1, 1) == (1, 1)? YES! Target reached.
        3. Return t = 4.
        """
        N, min_heap, visited = len(grid), [(grid[0][0], 0, 0)], {(0, 0)}
        
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))