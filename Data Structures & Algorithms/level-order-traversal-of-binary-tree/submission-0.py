class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        # We define the helper inside the main function to access 'levels' easily
        def helper(node, level):
            if not node:
                return
            
            # Create a new list for the new level
            if len(levels) == level:
                levels.append([])
            
            # Append node value to the correct level list
            levels[level].append(node.val)
            
            # Recurse to children
            helper(node.left, level + 1)
            helper(node.right, level + 1)
            
        helper(root, 0)
        return levels