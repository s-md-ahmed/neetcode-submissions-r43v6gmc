class Solution:
    """
    Dry Run Example: s = "12"
    Alright, you're locked in now. Let's finish that dry run for `s = "12"` exactly as the code executes it, step-by-step, with no skipping.

### Complete Step-by-Step Dry Run: `s = "12"`

1. **Initialization:** `dp = {2: 1}`. Call `dfs(0)`.
2. **`dfs(0)`:** * `0` in `dp`? No.
* `s[0]` is '1'. Not '0'.
* **Line: `res = dfs(1)**` (We must pause `dfs(0)` here).


3. **`dfs(1)`:** * `1` in `dp`? No.
* `s[1]` is '2'. Not '0'.
* **Line: `res = dfs(2)**` (Pause `dfs(1)`).


4. **`dfs(2)`:**
* `2` in `dp`? **Yes!** Return `1`.


5. **Back in `dfs(1)`:** * The `dfs(2)` call returned `1`. So `res` is now `1`.
* **Check 2 digits:** `if 1 + 1 < 2`: `2 < 2` is **False**.
* **Cache:** `dp[1] = 1`.
* **Return `1**` to `dfs(0)`.


6. **Back in `dfs(0)`:**
* The `dfs(1)` call finished and returned `1`. So `res` is now `1`.
* **Check 2 digits:** `if 0 + 1 < 2` (True) `and (s[0] == "1" or ...)` (True).
* **Line: `res += dfs(2)**`.


7. **`dfs(2)` (Second time):**
* `2` in `dp`? **Yes!** Return `1`.


8. **Back in `dfs(0)`:**
* We add the return value: `res = 1 + 1 = 2`.
* **Cache:** `dp[0] = 2`.
* **Return `2**`.
       
    """
    def numDecodings(self, s: str) -> int:
        # dp stores results of subproblems to avoid re-calculating (Memoization)
        dp = {len(s): 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            res=dfs(i+1)
            if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                res+=dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)