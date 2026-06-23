'''
Step,Call,Logic,preIdx,inIdx,inorder[inIdx],Limit,Action
1,dfs(inf),Create Node 3,1,0,9,inf,"root=3, left=dfs(3)"
2,dfs(3),Create Node 9,2,0,9,3,"root=9, left=dfs(9)"
3,dfs(9),9 == 9 (Limit),2,1,3,9,"inIdx becomes 1, return None"
4,dfs(3),3 == 3 (Limit),2,2,15,3,"inIdx becomes 2, return None"
5,dfs(inf),Create Node 20,3,2,15,inf,"root=20, left=dfs(20)"
6,dfs(20),Create Node 15,4,2,15,20,"root=15, left=dfs(15)"
7,dfs(15),15 == 15 (Limit),4,3,20,15,"inIdx becomes 3, return None"
8,dfs(20),Create Node 7,5,3,20,20,"root=7, left=dfs(7)"
9,dfs(7),20 != 7 (Wait!),5,3,20,7,"inIdx is 3, hits 20, None"
10,dfs(7),20 != 7 (Wait!),5,3,20,7,"inIdx is 3, hits 20, None"
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))