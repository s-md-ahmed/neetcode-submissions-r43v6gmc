class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_cheap = float('inf') # Professional way to say "99999"
        max_profit = 0
        
        for price in prices:
            # 1. Update the cheapest price we've found
            if price < curr_cheap:
                curr_cheap = price
            
            # 2. Calculate potential profit if we sold today
            potential_profit = price - curr_cheap
            
            # 3. Update max_profit if today's deal is better
            if potential_profit > max_profit:
                max_profit = potential_profit
                
        return max_profit