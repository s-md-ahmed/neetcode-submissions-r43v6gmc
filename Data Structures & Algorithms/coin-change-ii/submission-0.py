''' coin change 1 to coin change 2 shift
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize with a value larger than any possible answer
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # We can iterate amount, then coins
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    # Choose the minimum path
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        
        dp[0] = 1
        
        
        for c in coins:
            for i in range(c, amount + 1):
                
                dp[i] += dp[i - c]
        
        return dp[amount]