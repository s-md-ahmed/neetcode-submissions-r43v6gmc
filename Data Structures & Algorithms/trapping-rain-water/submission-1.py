class Solution:
    def trap(self, height: List[int]) -> int:
        amtwater=0
        tot=0
        for i in range(len(height)):
            # Providing a default of 0 prevents the crash on empty slices
            left_max = max(height[:i], default=0)
            right_max = max(height[i+1:], default=0)

            amtwater = max(0, min(left_max, right_max) - height[i])
            tot+=amtwater

        return tot
        
