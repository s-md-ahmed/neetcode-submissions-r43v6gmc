'''
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # Cache to store (r, c) -> longest path length starting from this cell

        def dfs(r, c):
            # If we already calculated the answer for this cell, just return it
            if (r, c) in dp:
                return dp[(r, c)]
            
            max_path = 1 # Every cell is a path of length 1 by itself
            
            # Check all 4 neighboring directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Condition: Must be in bounds AND the neighbor must have a STRICTLY GREATER value
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            # Save the result in our cache before returning
            dp[(r, c)] = max_path
            return max_path

        # Run DFS for every single cell in the grid and find the global maximum
        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))
'''
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # Cache to store (r, c) -> longest path length starting from this cell

        def dfs(r, c):
            # If we already calculated the answer for this cell, just return it
            if (r, c) in dp:
                return dp[(r, c)]
            
            max_path = 1 # Every cell is a path of length 1 by itself
            
            # Check all 4 neighboring directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Condition: Must be in bounds AND the neighbor must have a STRICTLY GREATER value
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            # Save the result in our cache before returning
            dp[(r, c)] = max_path
            return max_path

        # Run DFS for every single cell in the grid and find the global maximum
        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))