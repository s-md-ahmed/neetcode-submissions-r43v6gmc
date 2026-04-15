class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set() # This is our "guest list"
        for n in nums:
            if n in seen:
                return n # Found you!
            seen.add(n)