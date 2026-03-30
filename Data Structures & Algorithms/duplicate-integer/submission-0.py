class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums=set()
        for i in range(len(nums)):
            if nums[i] in seen_nums:
                return True
            else:
                seen_nums.add(nums[i])
        return False