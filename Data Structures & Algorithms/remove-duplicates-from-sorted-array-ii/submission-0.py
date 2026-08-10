class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        size = len(nums)
        
        if size <= 2:
            return size
            
        right = 2
        for i in range(2, size):
            if nums[i] != nums[right - 2]:
                nums[right] = nums[i]
                right += 1
                
        return right