''' 
Amount (i),Loop Coin (c),Condition i-c >= 0?,"Calculation: min(dp[i], 1 + dp[i-c])",Result
i=1,c=1,Yes (1−1=0),"min(7, 1 + dp[0]) = min(7, 1+0)",dp[1] = 1
,c=2,No (1−2=−1),Skip,-
i=2,c=1,Yes (2−1=1),"min(7, 1 + dp[1]) = min(7, 1+1)",dp[2] = 2
,c=2,Yes (2−2=0),"min(2, 1 + dp[0]) = min(2, 1+0)",dp[2] = 1
i=3,c=1,Yes (3−1=2),"min(7, 1 + dp[2]) = min(7, 1+1)",dp[3] = 2
,c=2,Yes (3−2=1),"min(2, 1 + dp[1]) = min(2, 1+1)",dp[3] = 2
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    # Update dp[i] if using this coin gives a smaller total
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        