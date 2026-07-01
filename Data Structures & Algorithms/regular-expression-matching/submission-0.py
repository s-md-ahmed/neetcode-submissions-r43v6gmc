class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        --- MINIMAL DRY RUN ---
        s = "a" (len=1), p = "ab*" (len=3)
        Start call: dfs(i=0, j=0)
        Note b* could mean 0 bs or 1 b or 2 b's and so on in our dry run since the star gave 0 b's 
        we got the perfect match of s and p
        
        ------------------------------------------------------------------------
        STEP 1: dfs(0, 0) -> Checking s[0]='a' and p[0]='a'
        ------------------------------------------------------------------------
        - match = (s[0] == p[0]) -> 'a' == 'a' -> True
        - Is p[1] == '*'? Look ahead to p[1]: It's 'b', NOT '*'.
        - Since there is no star right next to us, we take the standard path:
          Return dfs(i + 1, j + 1) -> Calls dfs(1, 1)

        ------------------------------------------------------------------------
        STEP 2: dfs(1, 1) -> Checking s index 1 (Out of bounds) and p[1]='b'
        ------------------------------------------------------------------------
        - match = (i < len(s)) -> 1 < 1 is False. So match = False.
        - Is p[2] == '*'? Look ahead to p[2]: Yes! It is '*'.
        - This triggers the Wildcard Branching Condition. We have two choices:
        
            Choice 1 (Skip the 'b*'):
              Call dfs(i, j + 2) -> dfs(1, 1 + 2) -> Calls dfs(1, 3)
              
            Choice 2 (Use the 'b*'):
              Requires 'match' to be True. But 'match' is False (string is empty).
              So this branch is ignored completely.

        ------------------------------------------------------------------------
        STEP 3: Inside the Choice 1 branch -> dfs(1, 3)
        ------------------------------------------------------------------------
        - j = 3, which equals len(p). We hit the base case!
        - Base case rule: return i == len(s) -> 1 == 1 -> True!
        
        ------------------------------------------------------------------------
        UNWINDING THE STACK:
        ------------------------------------------------------------------------
        - dfs(1, 3) returns True to dfs(1, 1)
        - dfs(1, 1) saves True in cache and returns True to dfs(0, 0)
        - dfs(0, 0) returns True to the main function
        
        Final Answer: True ("ab*" successfully matches "a" by turning "b*" into nothing!)
        ========================================================================
        """
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # The Wildcard Logic
            if (j + 1) < len(p) and p[j + 1] == '*':
                # If we see a star, we branch out. 
                # Either we skip 2 steps in the pattern, or we consume 1 char from s
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return False

        return dfs(0, 0)