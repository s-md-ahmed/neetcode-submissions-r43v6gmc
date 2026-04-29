class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        last_index = len(nums) - 1
    
        for i, jump in enumerate(nums):
            # If the current index 'i' is greater than the farthest index 
            # we've ever been able to reach, we are officially stuck.
            if i > farthest:
                return False
        
            # Update the furthest point reachabe from the current index
            farthest = max(farthest, i + jump)
        
            # Optimization: If we can touch or cross the finish line, we're done
            if farthest >= last_index:
                return True
                
        return farthest >= last_index