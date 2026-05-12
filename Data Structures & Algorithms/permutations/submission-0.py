class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        # The checklist to keep track of what's already in our path
        used = [False] * len(nums)
        
        def backtrack():
            # Base Case: Path is full
            if len(path) == len(nums):
                res.append(path[:]) # Create a copy!
                return
            
            for i in range(len(nums)):
                # Skip if the number at index 'i' is already being used
                if used[i]:
                    continue
                
                # --- The Sandwich ---
                used[i] = True         # 1. Action: Mark used
                path.append(nums[i])   # 2. Action: Add to path
                
                backtrack()            # 3. Recurse: Go to next level
                
                path.pop()             # 4. Undo: Remove from path
                used[i] = False        # 5. Undo: Mark as available
        
        backtrack()
        return res