class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        return math.comb(m + n - 2, m - 1)