class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        #0<5 0 to 1 farthest=2 l=1 r=2 res=1 2<5 
        #for i in range from 1 to 3 farthest=5 l=3 r=5 res=2
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res