"""
Dry Run: nums = [1, 5, 5]
Total = 11. Target = 5.5 (Wait, 11 is odd, returns False immediately)

Dry Run: nums = [1, 2, 3, 4]
Total = 10. Target = 5.
1. Start: possible_sums = {0}
2. num = 1: possible_sums = {0, 1}
3. num = 2: new_sums = {0+2, 1+2} = {2, 3}. possible_sums = {0, 1, 2, 3}
4. num = 3: new_sums = {0+3, 1+3, 2+3=5 (Target!)}. Returns True.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
            
        target = total // 2
        
        possible_sums = {0}
        
        for num in nums:
            new_sums = set()
            for s in possible_sums:
                
                if s + num == target:
                    return True
                
                if s + num < target:
                    new_sums.add(s + num)
            
            possible_sums.update(new_sums)
            
        return False