class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            # Removed abs() to save a function call
            area = min(heights[left], heights[right]) * (right - left)
            
            if maxar < area:
                maxar = area
                
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return maxar