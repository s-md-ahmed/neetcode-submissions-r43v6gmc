class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        #[1,2,3,4] res[0]=1 prefix=1 res[1]=1  prefix=2 res[2]=2 prefix=6 res[3]=6 prefix=24
        # The "Forward Slice" Snap
        prefix = 1
        for i in range(n):
            res[i] = prefix      
            prefix *= nums[i]    
            
        # The "Backward Slice" Snap [1,1,2,6]
        suffix = 1 #res[3]=6 suffix=4 res[2]= 8 suffix =12 res[1]=12 suffix=24 res[0]=24 suffix=24 
        for i in range(n - 1, -1, -1):
            res[i] *= suffix     
            suffix *= nums[i]    
        #res=24,12,8,6    
        return res