class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashval = {}
        
        # Step 1: Fill the dictionary with frequencies
        for n in nums:
            hashval[n] = 1 + hashval.get(n, 0)
            
        # Step 2: Iterate through the dictionary to find the one with count 1
        for key in hashval:
            if hashval[key] == 1:  # Check if the count (value) is 1
                return key