class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        path=[]
        visited=[False]*len(nums)
        def backtrack():
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                path.append(nums[i])
                visited[i]=True
                backtrack()
                path.pop()
                visited[i]=False
        backtrack()
        return res

        