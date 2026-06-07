'''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return math.comb(m + n - 2, m - 1)'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        
        for i in range(1, m):
            for j in range(1, n):
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        
        return dp[m-1][n-1]