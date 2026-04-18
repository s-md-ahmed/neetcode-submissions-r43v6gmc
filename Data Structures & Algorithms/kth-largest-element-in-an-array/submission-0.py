import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Example: nums = [2, 3, 1, 5, 4], k = 2
        minheap = []
        
        for n in nums:
            heapq.heappush(minheap, n)
            
            # DRY RUN TRACE:
            # 1. n=2: heap=[2] (len 1 <= 2)
            # 2. n=3: heap=[2, 3] (len 2 <= 2)
            # 3. n=1: heap=[1, 2, 3] -> heappop -> heap=[2, 3] (kicked out 1)
            # 4. n=5: heap=[2, 3, 5] -> heappop -> heap=[3, 5] (kicked out 2)
            # 5. n=4: heap=[3, 4, 5] -> heappop -> heap=[4, 5] (kicked out 3)
            
            if len(minheap) > k:
                heapq.heappop(minheap)
                
        # Final heap contains [4, 5], smallest is 4
        return minheap[0]