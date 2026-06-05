class Solution:
    def countSubstrings(self, s: str) -> int:
        def countpalin(l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        count=0
        res1=0
        for i in range(len(s)):
            l=r=i
            count+=countpalin(l,r)
            l=i
            r=i+1
            res1+=countpalin(l,r)

            
        return count+res1
        