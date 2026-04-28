class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''hashval = {}
        
        
        for n in nums:
            hashval[n] = 1 + hashval.get(n, 0)
            
        
        for key in hashval:
            if hashval[key] == 1:  # Check if the count (value) is 1
                return key'''
        ans=0
        for n in nums:
            ans^=n
        return ans