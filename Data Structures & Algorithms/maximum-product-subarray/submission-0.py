class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # nums = [2,4,-3,5] res=5 tmp=2 curmax=max(2,2,2)
        # curmin=min(2,2,2)
        # res=max(5,2)
        # i=1 tmp=2*4=8, curmax=max(4*2,4*2,4) curmin=min(8,4*2,4) res=max(5,8)
        # i=2 tmp=8*-3=-24 curmax=(-24,-12,-3) curmin=min(-24,-12,-3) res= max(8,-3)
        # i=3 tmp=-3*5=-15 curmax=max(-15,-120,5) curmin=min(-15,-120,5) res=max(8,5)=8
        
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
                
            
            tmp = curMax * n
            
            
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            
            res = max(res, curMax)
            
        return res