# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0 
            
            
            left_h = check(node.left)
            if left_h == -1: return -1 
            
            
            right_h = check(node.right)
            if right_h == -1: return -1 
            
            
            if abs(left_h - right_h) > 1:
                return -1 # Mark as broken
            
            
            return 1 + max(left_h, right_h)

        
        return check(root) != -1
        