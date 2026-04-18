import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []
        
        for s in stones:
            heapq.heappush(minheap, -s)
            
        for i in range(len(stones)):
            if len(minheap) > 1:
                first = -heapq.heappop(minheap)
                second = -heapq.heappop(minheap)
                
                if first != second:
                    heapq.heappush(minheap, -(first - second))
            else:
                break
        
        return -minheap[0] if minheap else 0