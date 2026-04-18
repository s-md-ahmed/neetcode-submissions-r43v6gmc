import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k=k
        self.minimheap=[]
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.minimheap)<self.k:
            heapq.heappush(self.minimheap,val)
        elif val>self.minimheap[0]:
            heapq.heapreplace(self.minimheap,val)
            
        
        return self.minimheap[0]