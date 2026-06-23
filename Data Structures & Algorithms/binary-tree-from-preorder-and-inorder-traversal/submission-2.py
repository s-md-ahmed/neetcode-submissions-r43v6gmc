class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if there's nothing to build, return None
        if not preorder or not inorder:
            return None
        
        # 1. The first node in preorder is ALWAYS the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. Find the root's position in the inorder list
        # This split point tells us exactly what belongs on the left vs right
        mid = inorder.index(root_val)
        
        # 3. Create the left subtree using the left "chunk" of inorder
        # We also need to slice the preorder list accordingly
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # 4. Create the right subtree using the right "chunk" of inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root