class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        DRY RUN: heights = [7, 1, 7, 2, 2, 4] (Appended with 0 at the end)
        
        | i | heights[i] | Stack (indices) | Pop? | h (popped) | w (i - stack[-1] - 1) | Area | Max |
        |---|------------|-----------------|------|------------|-----------------------|------|-----|
        | 0 | 7          | [-1, 0]         | No   | -          | -                     | -    | 0   |
        | 1 | 1          | [-1]            | Yes  | 7          | 1 - (-1) - 1 = 1      | 7    | 7   |
        | 1 | 1          | [-1, 1]         | No   | -          | -                     | -    | 7   |
        | 2 | 7          | [-1, 1, 2]      | No   | -          | -                     | -    | 7   |
        | 3 | 2          | [-1, 1]         | Yes  | 7          | 3 - 1 - 1 = 1         | 7    | 7   |
        | 3 | 2          | [-1, 1, 3]      | No   | -          | -                     | -    | 7   |
        | 4 | 2          | [-1, 1, 3]      | Yes  | 2          | 4 - 1 - 1 = 2         | 4    | 7   |
        | 4 | 2          | [-1, 1, 4]      | No   | -          | -                     | -    | 7   |
        | 5 | 4          | [-1, 1, 4, 5]   | No   | -          | -                     | -    | 7   |
        | 6 | 0 (ghost)  | [-1, 1, 4]      | Yes  | 4          | 6 - 4 - 1 = 1         | 4    | 7   |
        | 6 | 0 (ghost)  | [-1, 1]         | Yes  | 2          | 6 - 1 - 1 = 4         | 8    | 8   |
        | 6 | 0 (ghost)  | [-1]            | Yes  | 1          | 6 - (-1) - 1 = 6      | 6    | 8   |
        |---|------------|-----------------|------|------------|-----------------------|------|-----|
        """
        
        # Add a 0 to force the stack to empty at the end
        heights.append(0)
        # -1 acts as a boundary so we don't have to check if stack is empty
        stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        
        heights.pop() 
        return max_area