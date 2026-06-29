class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        TOTAL UNABRIDGED RECURSION TREE DRY RUN: nums = [3, 1, 5]
        Padded Array: A = [1, 3, 1, 5, 1], Initial Call: dfs(1, 3)

        Every branch, every subproblem, and every index 'i' mapped out fully:

        dfs(1, 3)
         ├── i = 1 (value 3)
         │    ├── base = A[0]*A[1]*A[4] = 1*3*1 = 3
         │    ├── left = dfs(1, 0) ──> 0 (1 > 0)
         │    └── right = dfs(2, 3)
         │         ├── i = 2 (value 1)
         │         │    ├── base = A[1]*A[2]*A[4] = 3*1*1 = 3
         │         │    ├── left = dfs(2, 1) ──> 0 (2 > 1)
         │         │    └── right = dfs(3, 3)
         │         │         ├── i = 3 (value 5)
         │         │         │    ├── base = A[2]*A[3]*A[4] = 1*5*1 = 5
         │         │         │    ├── left = dfs(3, 2) ──> 0 (3 > 2)
         │         │         │    └── right = dfs(4, 3) ──> 0 (4 > 3)
         │         │         └── Returns: 5 + 0 + 0 = 5
         │         │    └── Total for i = 2: 3 + 0 + 5 = 8
         │         │
         │         ├── i = 3 (value 5)
         │         │    ├── base = A[1]*A[3]*A[4] = 3*5*1 = 15
         │         │    ├── left = dfs(2, 2)
         │         │    │    ├── i = 2 (value 1)
         │         │    │    │    ├── base = A[1]*A[2]*A[3] = 3*1*5 = 15
         │         │    │    │    ├── left = dfs(2, 1) ──> 0 (2 > 1)
         │         │    │    │    └── right = dfs(3, 2) ──> 0 (3 > 2)
         │         │    │    └── Returns: 15 + 0 + 0 = 15
         │         │    └── right = dfs(4, 3) ──> 0 (4 > 3)
         │         │    └── Total for i = 3: 15 + 15 + 0 = 30
         │         │
         │         └── dfs(2, 3) Max Choice: max(8, 30) = 30 [CACHED]
         │    └── Total for i = 1: 3 + 0 + 30 = 33
         │
         ├── i = 2 (value 1)
         │    ├── base = A[0]*A[2]*A[4] = 1*1*1 = 1
         │    ├── left = dfs(1, 1)
         │    │    ├── i = 1 (value 3)
         │    │    │    ├── base = A[0]*A[1]*A[2] = 1*3*1 = 3
         │    │    │    ├── left = dfs(1, 0) ──> 0 (1 > 0)
         │    │    │    └── right = dfs(2, 1) ──> 0 (2 > 1)
         │    │    └── Returns: 3 + 0 + 0 = 3 [CACHED]
         │    └── right = dfs(3, 3) ──> Returns 5 [CACHED FROM ABOVE]
         │    └── Total for i = 2: 1 + 3 + 5 = 9
         │
         ├── i = 3 (value 5)
         │    ├── base = A[0]*A[3]*A[4] = 1*5*1 = 5
         │    ├── left = dfs(1, 2)
         │    │    ├── i = 1 (value 3)
         │    │    │    ├── base = A[0]*A[1]*A[3] = 1*3*5 = 15
         │    │    │    ├── left = dfs(1, 0) ──> 0 (1 > 0)
         │    │    │    └── right = dfs(2, 2) ──> Returns 15 [CACHED FROM ABOVE]
         │    │    │    └── Total for i = 1: 15 + 0 + 15 = 30
         │    │    │
         │    │    ├── i = 2 (value 1)
         │    │    │    ├── base = A[0]*A[2]*A[3] = 1*1*5 = 5
         │    │    │    ├── left = dfs(1, 1) ──> Returns 3 [CACHED FROM ABOVE]
         │    │    │    └── right = dfs(3, 2) ──> 0 (3 > 2)
         │    │    │    └── Total for i = 2: 5 + 3 + 0 = 8
         │    │    │
         │    │    └── dfs(1, 2) Max Choice: max(30, 8) = 30 [CACHED]
         │    ├── right = dfs(4, 3) ──> 0 (4 > 3)
         │    └── Total for i = 3: 5 + 30 + 0 = 35
         │
         └── dfs(1, 3) Absolute Max: max(33, 9, 35) = 35
        """
        A = [1] + nums + [1]
        memo = {}
        
        def dfs(l, r):
            if l > r:
                return 0    
            if (l, r) in memo:
                return memo[(l, r)]
            max_coins = 0
            for i in range(l, r + 1):    
                coins = A[l - 1] * A[i] * A[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                max_coins = max(max_coins, coins)
            memo[(l, r)] = max_coins
            return max_coins
            
        return dfs(1, len(nums))