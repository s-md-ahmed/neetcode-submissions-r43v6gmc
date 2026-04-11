class Solution:
    """
    DRY RUN 1: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 (Left Sorted Case)
    | Iter | low | high | mid | nums[mid] | Sorted Half | Decision         | Next Range  |
    |------|-----|------|-----|-----------|-------------|------------------|-------------|
    | 1    | 0   | 6    | 3   | 7         | Left (4<=7) | 0 not in [4,7)   | low = 4     |
    | 2    | 4   | 6    | 5   | 1         | Left (0<=1) | 0 not in [0,1)   | high = 4    |
    | 3    | 4   | 4    | 4   | 0         | Found!      | return mid (4)   | Done        |

    DRY RUN 2: nums = [6, 7, 0, 1, 2, 4, 5], target = 7 (Right Sorted Case)
    | Iter | low | high | mid | nums[mid] | Sorted Half  | Decision        | Next Range  |
    |------|-----|------|-----|-----------|--------------|-----------------|-------------|
    | 1    | 0   | 6    | 3   | 1         | Right (1<=5) | 7 not in (1,5]  | high = 2    |
    | 2    | 0   | 2    | 1   | 7         | Found!       | return mid (1)  | Done        |
    """
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # CASE 1: Left Side [low...mid] is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  
                else:
                    low = mid + 1   
            
            # CASE 2: Right Side [mid...high] is sorted
            else:
                
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   
                else:
                    high = mid - 1  
                    
        return -1