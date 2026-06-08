class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: 
            return 0
        
        # dp[day][state]
        # state 0: holding
        # state 1: sold/cooldown
        # state 2: reset/available
        dp = [[0] * 3 for _ in range(n)]
        
        # Base case: Day 0
        dp[0][0] = -prices[0] # Bought on day 0
        dp[0][1] = 0          # Cannot sell on day 0
        dp[0][2] = 0          # Reset state, no profit yet
        
        for i in range(1, n):
            # 1. HOLDING: Either I was holding yesterday, or I bought today (using reset cash)
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            
            # 2. SOLD/COOLDOWN: I must have held yesterday and sold today
            dp[i][1] = dp[i-1][0] + prices[i]
            
            # 3. RESET/AVAILABLE: Either I was already reset, or I just finished cooldown
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
            
        # The answer is the max cash I have left (either just sold or sitting in reset)
        return max(dp[n-1][1], dp[n-1][2])