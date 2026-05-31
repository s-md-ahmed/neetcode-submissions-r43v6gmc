# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def findsame(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and not node2 or not node1 and node2:
                return False
            if node1.val==node2.val:
                return findsame(node1.left,node2.left) and findsame(node1.right,node2.right)
        return findsame(root,subroot) or self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
            
        