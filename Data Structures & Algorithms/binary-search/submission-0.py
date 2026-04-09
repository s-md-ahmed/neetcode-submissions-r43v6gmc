class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # Shift the midpoint to the right if there's an even number of elements
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1 # Target is in the right half
            else:
                r = mid - 1 # Target is in the left half
                
        return -1 # Target isn't in the list