class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_cheap = float('inf') # Professional way to say "99999"
        max_profit = 0
        left=0
        right=1
        while right<len(prices):
            curr_profit=prices[right]-prices[left]
            if curr_profit>max_profit:
                max_profit=curr_profit
            if curr_profit<0:
                left=right
            right+=1
            
                
        return max_profit