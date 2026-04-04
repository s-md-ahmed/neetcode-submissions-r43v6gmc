class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxnums=[]
        left=0
        right=k-1
        n=len(nums)
        print(nums)
        for i in range(0,n-k+1):
            highval=max(nums[left:right+1])
            maxnums.append(highval)
            left+=1
            right+=1
        return maxnums

        