class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numcheck = set(nums)
        longest_streak = 0
        
        for num in numcheck:
            if num - 1 not in numcheck:
                current_num = num
                current_streak = 1
                
                
                while current_num + 1 in numcheck:
                    current_num += 1
                    current_streak += 1
                
                
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak