class Solution:
    '''
    Iteration,low,high,mid,nums[mid],nums[high],Condition nums[mid] > nums[high],Action
1,0,5,2,5,2,5>2 (True),low = mid + 1 (low = 3)
2,3,5,4,1,2,1>2 (False),high = mid (high = 4)
3,3,4,3,6,1,6>1 (True),low = mid + 1 (low = 4)
End,4,4,-,-,-,Loop terminates,return nums[low] (nums[4] = 1)
    '''
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2  
            
            if nums[mid] > nums[high]:
                
                low = mid + 1
            else:
                
                high = mid
                
        return nums[low]