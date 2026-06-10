''' Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
nextDp=True 4<4 twice also false res= True dp[4]=True nextDp=dp[4](True)
res=False as 3<4 4<4 false 3<4 and s2[3]=b == s3[3+4]=a false dp
res=false as 2<4 and s2[2]==s2[4+2] b==a no
res=false as 1<4 and s2[1]=b==s3[4+1]=s3[5]=b true res=True  dp[1]=1=True nextdp=True
res=false as 0<4 s2[0]==s3[0+4] True res=True again dp[0] True nextDp=True
now i=3 nextDp now becomes false as 3==4 is false j starts from 4 4<4 no 3<4 yes s1[3]==s1[3+4] yes so res=true 4<4 no  so res=nextdp which is also true dp and nextdp both true
now i=3 j=3 3<4 so res is false 3<4 yes s1[3]==s1[3+3] yes so res=True 3<4 yes and s2[3]==s3[3+3] no so again dp and nextdp both true
now j=2 res=false as j=2 3<4 yes s1[3]==s1[3+2] no 2<4 yeah s2[2]==s3[2+3] yes so dp and nextdp both r true so this process continues til u get dp of 0 and if dp of 0 is false the utput is false else dp of 0 istrue means u get true
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            nextDp = True if i == m else False
            for j in range(n, -1, -1):
                res = False if j < n else nextDp
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    res = True
                if j < n and s2[j] == s3[i + j] and nextDp:
                    res = True
                dp[j] = res
                nextDp = dp[j]
        return dp[0]