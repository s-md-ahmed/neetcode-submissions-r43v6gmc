'''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxnums=[]
        left=0
        right=k-1
        n=len(nums)
        print(nums)
        for i in range(0,n-k+1):
            highval=max(nums[left:right+1])
            maxnums.append(highval)
            left+=1
            right+=1 the above solution is good but not optimized
        return maxnums'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        DRY RUN: nums = [1, 3, -1, -3, 5], k = 3
        
        Step (right) | val | Bully (Pop Back) | Expire (Pop Front) | dq (indices) | dq (values) | Result
        ---------------------------------------------------------------------------------------------
        0            | 1   | Empty            | left=-2. No pop.   | [0]          | [1]         | Wait...
        1            | 3   | 3 > 1. Pop idx 0 | left=-1. No pop.   | [1]          | [3]         | Wait...
        2            | -1  | -1 < 3. No pop   | left=0. No pop.    | [1, 2]       | [3, -1]     | [3]
        3            | -3  | -3 < -1. No pop  | left=1. No pop.    | [1, 2, 3]    | [3, -1, -3] | [3, 3]
        4            | 5   | 5 > all. Pop all | left=2. No pop.    | [4]          | [5]         | [3, 3, 5]
        """
        
        maxnums = []
        n = len(nums)
        dq = deque()  # Stores indices of potential maximums
        
        for right in range(n):
            # 1. THE BULLY RULE:
            # If the current number is bigger than what's at the back, 
            # the back elements can NEVER be the max (they are smaller AND older).
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            # Add current index to the queue
            dq.append(right)
            
            # 2. THE EXPIRATION RULE:
            # Calculate where the current window starts.
            # If the index at the front of dq is smaller than 'left', it's out.
            left = right - k + 1
            if dq[0] < left:
                dq.popleft()
            
            # 3. THE STORAGE RULE:
            # Once we've reached the first full window (index k-1), 
            # the front of the dq is ALWAYS our current highval.
            if right >= k - 1:
                maxnums.append(nums[dq[0]])
                
        return maxnums
        