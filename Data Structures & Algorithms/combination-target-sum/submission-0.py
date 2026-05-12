class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i, current_path, current_total):
            # Success base case
            if current_total == target:
                res.append(list(current_path))
                return
            
            # Failure base case (went over target or out of bounds)
            if i >= len(nums) or current_total > target:
                return

            # Option 1: Include nums[i]
            # We don't increment 'i' because we can use the same number again
            current_path.append(nums[i])
            backtrack(i, current_path, current_total + nums[i])
            
            # Backtrack step: remove the number so we can try Option 2
            current_path.pop()

            # Option 2: Exclude nums[i]
            # Move to the next number
            backtrack(i + 1, current_path, current_total)

        backtrack(0, [], 0)
        return res