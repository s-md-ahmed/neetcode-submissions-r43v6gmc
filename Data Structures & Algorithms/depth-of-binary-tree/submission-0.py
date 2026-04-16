# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftdepth=self.maxDepth(root.left)
        rightdepth=self.maxDepth(root.right)
        maxim=max(leftdepth,rightdepth)
        return maxim+1#add plus one so that the root gets counted too else root gets ghosted and u always get 0