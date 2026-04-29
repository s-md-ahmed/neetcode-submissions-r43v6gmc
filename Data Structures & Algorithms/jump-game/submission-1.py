class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        last_index = len(nums) - 1
    
        for i in range(len(nums)):
            # 1. Check if we've been left behind
            # If our current index i is beyond our maximum reach (farthest),
            # it means we hit a 0 earlier and can't move forward.
            if i > farthest:
                return False
        
            # 2. Update our "horizon"
            # We see how far we can jump from the current spot (i + nums[i])
            # and compare it to the best jump we found previously.
            if i + nums[i] > farthest:
                farthest = i + nums[i]
        
            # 3. Early Exit
            # If our horizon already reaches or passes the last index, we win!
            if farthest >= last_index:
                return True
        
        # This line is a fallback. If the loop finishes, we check one last time
        # if our reach made it to the finish line.
        return farthest >= last_index