class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))#to exclude last index and first index 