class Solution:

  def maxArea(self, heights: list[int]) -> int:
    maxar = 0
    left, right = 0, len(heights) - 1  

    while left < right:
      
      width = right - left
      current_height = min(heights[left], heights[right])
      area = width * current_height

      
      maxar = max(maxar, area)

      
      if heights[left] < heights[right]:
        left += 1
      else:
        right -= 1

    return maxar