class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS={}
        countT={}
        for char in s:
            countS[char]=1+countS.get(char,0)
        for char1 in t:
            countT[char1]=1+countT.get(char1,0)
        if countS==countT:
            return True
        return False