class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        # We track current_sum instead of subtracting from target
        def backtrack(i, current_path, current_sum):
            # Success: Goal reached
            if current_sum == target:
                res.append(list(current_path))
                return#jumps to the last line of the function always
            
            # Failure: Exceeded target or out of bounds
            if current_sum > target:
                return

            for j in range(i, len(candidates)):
                # Still use the skip logic to avoid duplicates
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                # Make choice
                current_path.append(candidates[j])
                
                # Recurse: Move to next index (j + 1) and add to sum
                backtrack(j + 1, current_path, current_sum + candidates[j])
                
                # Undo choice (Backtrack)
                current_path.pop()

        backtrack(0, [], 0)
        return res