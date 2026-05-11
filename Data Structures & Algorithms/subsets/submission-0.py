class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            # -------------------------------------------------------
            # FULL DRY RUN FOR nums = [1, 2, 3] | len = 3
            # -------------------------------------------------------
            # 1.  dfs(0): Include 1 -> subset: [1]. Call dfs(1)
            # 2.    dfs(1): Include 2 -> subset: [1, 2]. Call dfs(2)
            # 3.      dfs(2): Include 3 -> subset: [1, 2, 3]. Call dfs(3)
            # 4.        dfs(3): BASE CASE! res: [[1, 2, 3]]. RETURN to 3.
            # 5.      dfs(2): Pop 3 -> subset: [1, 2]. Call dfs(3)
            # 6.        dfs(3): BASE CASE! res: [[1, 2, 3], [1, 2]]. RETURN to 5.
            #
            # 7.    dfs(1): Pop 2 -> subset: [1]. Call dfs(2) (The "Exclude 2" branch)
            # 8.      dfs(2): Include 3 -> subset: [1, 3]. Call dfs(3)
            # 9.        dfs(3): BASE CASE! res: [..., [1, 3]]. RETURN to 8.
            # 10.     dfs(2): Pop 3 -> subset: [1]. Call dfs(3)
            # 11.       dfs(3): BASE CASE! res: [..., [1]]. RETURN to 10.
            #
            # 12. dfs(0): Pop 1 -> subset: []. Call dfs(1) (The "Exclude 1" branch)
            # 13.   dfs(1): Include 2 -> subset: [2]. Call dfs(2)
            # 14.     dfs(2): Include 3 -> subset: [2, 3]. Call dfs(3)
            # 15.       dfs(3): BASE CASE! res: [..., [2, 3]]. RETURN to 14.
            # 16.     dfs(2): Pop 3 -> subset: [2]. Call dfs(3)
            # 17.       dfs(3): BASE CASE! res: [..., [2]]. RETURN to 16.
            #
            # 18.   dfs(1): Pop 2 -> subset: []. Call dfs(2) (The "Exclude 2" branch)
            # 19.     dfs(2): Include 3 -> subset: [3]. Call dfs(3)
            # 20.       dfs(3): BASE CASE! res: [..., [3]]. RETURN to 19.
            # 21.     dfs(2): Pop 3 -> subset: []. Call dfs(3)
            # 22.       dfs(3): BASE CASE! res: [..., []]. RETURN to 21.
            # -------------------------------------------------------

            if i >= len(nums):
                res.append(subset[:]) # Snapshot the current "reality"
                return

            # Decision: Include nums[i] (Going Left on the Tree)
            subset.append(nums[i])
            dfs(i + 1)

            # Decision: Exclude nums[i] (Going Right on the Tree)
            subset.pop() # The "Undo" button
            dfs(i + 1)

        dfs(0)
        return res