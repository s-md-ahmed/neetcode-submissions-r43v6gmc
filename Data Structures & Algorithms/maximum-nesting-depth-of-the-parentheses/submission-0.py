class Solution:
    def maxDepth(self, s: str) -> int:
        s1=[]
        val=0
        for i in range(len(s)):
            if s[i]=='(':
                val+=1
                s1.append(val)
            if s[i]==')':
                val-=1
                s1.append(val)
        print(s1)
        fin=int(max(s1,default=0))
        print(fin)
        return fin  