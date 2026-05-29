class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # 1. Sort the list to bring duplicates together
        nums.sort()
        result = []
        
        # 2. Define the backtracking function
        def backtrack(start, current_subset):
            # 3. Add a copy of the current subset to results
            result.append(list(current_subset))
            
            # 4. Loop through the remaining elements
            for i in range(start, len(nums)):
                # 5. Skip duplicates: If it's the same as the previous 
                # element and not the first one in this loop, skip it.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # 6. Include the element
                current_subset.append(nums[i])
                
                # 7. Recurse to build further
                backtrack(i + 1, current_subset)
                
                # 8. Backtrack: remove the element to try the next one
                current_subset.pop()
                
        # Start the process
        backtrack(0, [])
        return result