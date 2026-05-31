class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node, maxval):
            nonlocal count # This tells Python to use the 'count' from above
            if not node:
                return
            
            if node.val >= maxval:
                count += 1 
                maxval = node.val 
            
            dfs(node.left, maxval)
            dfs(node.right, maxval)
            
        dfs(root, float('-inf'))
        return count