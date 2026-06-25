class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1): #this loop is for k stops else if only inner loop wa sthere it would work for only 1 stop
            temp_prices = prices[:]
            
            for s, d, p in flights:
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
            
        return prices[dst] if prices[dst] != float("inf") else -1