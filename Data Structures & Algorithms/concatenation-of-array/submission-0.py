class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newar=[]
        for i in range(len(nums)):
            newar.append(nums[i])
        for num in nums:
            newar.append(num)
        return newar