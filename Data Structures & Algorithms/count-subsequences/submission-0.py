class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Calculates the number of distinct subsequences of s which equals t.
        
        ========================================================================
        DETAILED DRY RUN
        ========================================================================
        s = "rabbbit" (len = 7), t = "rabbit" (len = 6)
        
        Initial dp array of size 7:
        Index:    0    1    2    3    4    5    6
        t char:  ''   'r'  'a'  'b'  'b'  'i'  't'
        dp:      [1,   0,   0,   0,   0,   0,   0]
        
        ------------------------------------------------------------------------
        OUTER LOOP 1: char_s = 'r'
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'r' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'r' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 'r' == 'b' -> False. No change.
        - j = 2 (t[2]='b'): 'r' == 'b' -> False. No change.
        - j = 1 (t[1]='a'): 'r' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 'r' == 'r' -> True!  dp[1] += dp[0] -> 0 + 1 = 1
        State after Loop 1: [1, 1, 0, 0, 0, 0, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 2: char_s = 'a'
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'a' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'a' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 'a' == 'b' -> False. No change.
        - j = 2 (t[2]='b'): 'a' == 'b' -> False. No change.
        - j = 1 (t[1]='a'): 'a' == 'a' -> True!  dp[2] += dp[1] -> 0 + 1 = 1
        - j = 0 (t[0]='r'): 'a' == 'r' -> False. No change.
        State after Loop 2: [1, 1, 1, 0, 0, 0, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 3: char_s = 'b' (First 'b' in s)
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'b' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'b' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 'b' == 'b' -> True!  dp[4] += dp[3] -> 0 + 0 = 0
        - j = 2 (t[2]='b'): 'b' == 'b' -> True!  dp[3] += dp[2] -> 0 + 1 = 1
        - j = 1 (t[1]='a'): 'b' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 'b' == 'r' -> False. No change.
        State after Loop 3: [1, 1, 1, 1, 0, 0, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 4: char_s = 'b' (Second 'b' in s)
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'b' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'b' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 'b' == 'b' -> True!  dp[4] += dp[3] -> 0 + 1 = 1
        - j = 2 (t[2]='b'): 'b' == 'b' -> True!  dp[3] += dp[2] -> 1 + 1 = 2
        - j = 1 (t[1]='a'): 'b' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 'b' == 'r' -> False. No change.
        State after Loop 4: [1, 1, 1, 2, 1, 0, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 5: char_s = 'b' (Third 'b' in s)
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'b' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'b' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 'b' == 'b' -> True!  dp[4] += dp[3] -> 1 + 2 = 3
        - j = 2 (t[2]='b'): 'b' == 'b' -> True!  dp[3] += dp[2] -> 2 + 1 = 3
        - j = 1 (t[1]='a'): 'b' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 'b' == 'r' -> False. No change.
        State after Loop 5: [1, 1, 1, 3, 3, 0, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 6: char_s = 'i'
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 'i' == 't' -> False. No change.
        - j = 4 (t[4]='i'): 'i' == 'i' -> True!  dp[5] += dp[4] -> 0 + 3 = 3
        - j = 3 (t[3]='b'): 'i' == 'b' -> False. No change.
        - j = 2 (t[2]='b'): 'i' == 'b' -> False. No change.
        - j = 1 (t[1]='a'): 'i' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 'i' == 'r' -> False. No change.
        State after Loop 6: [1, 1, 1, 3, 3, 3, 0]

        ------------------------------------------------------------------------
        OUTER LOOP 7: char_s = 't'
        ------------------------------------------------------------------------
        - j = 5 (t[5]='t'): 't' == 't' -> True!  dp[6] += dp[5] -> 0 + 3 = 3
        - j = 4 (t[4]='i'): 't' == 'i' -> False. No change.
        - j = 3 (t[3]='b'): 't' == 'b' -> False. No change.
        - j = 2 (t[2]='b'): 't' == 'b' -> False. No change.
        - j = 1 (t[1]='a'): 't' == 'a' -> False. No change.
        - j = 0 (t[0]='r'): 't' == 'r' -> False. No change.
        State after Loop 7: [1, 1, 1, 3, 3, 3, 3]

        Final Return Value: dp[-1] = 3
        ========================================================================
        """
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(len(t) - 1, -1, -1):
                if char_s == t[j]:
                    dp[j + 1] += dp[j]

        return dp[-1]