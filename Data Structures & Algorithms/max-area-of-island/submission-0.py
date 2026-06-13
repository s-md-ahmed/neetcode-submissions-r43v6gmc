class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,cols=len(grid),len(grid[0])
        maxc=0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        for r in range(row):
            for c in range(cols):
                counter=dfs(r,c)
                maxc=max(maxc,counter)
        return maxc