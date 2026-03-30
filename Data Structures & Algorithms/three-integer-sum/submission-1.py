class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pivot=nums[0] #[-4,-1,-1,0,1,2]
        thrsum=[]
        left,right=1,len(nums)-1
        idx=0
        for i in range(0,len(nums)):
            if nums[i] > 0: # If the smallest number is > 0, sum can never be 0
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            pivot=nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if pivot+nums[left]+nums[right]==0:
                    thrsum.append([pivot,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif pivot+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1
        return thrsum
                

