class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DRY RUN: text1 = "abc", text2 = "ac"
        Initial: text1="abc", text2="ac", dp=[0, 0, 0]
        
        i=2 ('c'):
           j=1 ('c'): Match! dp[1] = 1 + prev(0) = 1. prev = temp(0)
           j=0 ('a'): No match. dp[0] = max(dp[0]=0, dp[1]=1) = 1. prev = temp(0)
           dp is now [1, 1, 0]
        
        i=1 ('b'):
           j=1 ('c'): No match. dp[1] = max(dp[1]=1, dp[2]=0) = 1. prev = temp(1)
           j=0 ('a'): No match. dp[0] = max(dp[0]=1, dp[1]=1) = 1. prev = temp(1)
           dp is now [1, 1, 0]
           
        i=0 ('a'):
           j=1 ('c'): No match. dp[1] = max(dp[1]=1, dp[2]=0) = 1. prev = temp(1)
           j=0 ('a'): Match! dp[0] = 1 + prev(1) = 2. prev = temp(1)
           dp is now [2, 1, 0]
           
        Result: dp[0] = 2
        """
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp

        return dp[0]