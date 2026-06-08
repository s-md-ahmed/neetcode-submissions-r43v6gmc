'''
To understand the length of dp, let's walk through your specific example: 
nums = [2, 2, 2], target = 2.1. Calculating the subset_targettotal_sum = $2 + 2 + 2 = 6$
subset_target = $(target + total\_sum) // 2$ = $(2 + 6) // 2 = 8 // 2 = \mathbf{4}$2. 
The dp Array LengthThe line dp = [0] * (subset_target + 1) creates an array of size $4 + 1 = \mathbf{5}$.
The indices are [0, 1, 2, 3, 4].3. 
Stepping through the logic Initially: dp = [1, 0, 0, 0, 0] (There is 1 way to make sum 0).
First num (2):dp[4] += dp[4-2] $\rightarrow$ dp[4] = 0 + dp[2] = 0dp[3] += dp[3-2] $\rightarrow$ dp[3] = 0 + dp[1] = 0dp[2] += dp[2-2] $\rightarrow$ dp[2] = 0 + 1 = 1dp is now: [1, 0, 1, 0, 0]
Second num (2):dp[4] += dp[4-2] $\rightarrow$ dp[4] = 0 + dp[2] = 1dp[3] += dp[3-2] $\rightarrow$ dp[3] = 0 + dp[1] = 0dp[2] += dp[2-2] $\rightarrow$ dp[2] = 1 + 1 = 2dp is now: [1, 0, 2, 0, 1]
Third num (2):dp[4] += dp[4-2] $\rightarrow$ dp[4] = 1 + dp[2] = $1 + 2 = \mathbf{3}$dp[3] += dp[3-2] $\rightarrow$ dp[3] = 0 + dp[1] = 0dp[2] += dp[2-2] $\rightarrow$ dp[2] = 2 + 1 = 3dp is now: [1, 0, 3, 0, 3]
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Edge cases: 
        # 1. If target is out of range
        # 2. If (target + total_sum) is odd, we can't divide it by 2
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        subset_target = (target + total_sum) // 2
        
        # Now solve standard "Subset Sum" problem
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # One way to make sum 0: pick nothing
        
        for num in nums:
            # Iterate backwards to ensure each number is used only once (0/1 Knapsack)
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_target]