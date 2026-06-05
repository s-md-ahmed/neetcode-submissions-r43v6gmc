class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for mid in range(len(s)):
            
            l, r = mid, mid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1  
                r += 1  

            
            l, r = mid, mid + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l : r + 1]
                l -= 1  
                r += 1  
                
        return res