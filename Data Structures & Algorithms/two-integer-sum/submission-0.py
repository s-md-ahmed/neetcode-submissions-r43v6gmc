class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums={}
        complement=0
        for i in range (len(nums)):
            num=nums[i]
            complement=target-num
            if complement in seen_nums:
                return [seen_nums[complement],i]
            else:
                seen_nums[num]=i
        return []