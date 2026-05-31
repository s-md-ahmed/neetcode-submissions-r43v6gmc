# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#DRY RUN root = [1,2,3,4,null,null,null,5] 
'''node=1 myq=[2,3] i=0==1-1 yes so reuslt will take in 1
levelsize=2 node=2 myq=[3,4] i=0==2-1 no 
queue becomes 3 popped out so myq=4  and i=1 3 does not have a left and right so print in 3
levelsize is 1 for 0 in range of 1 node=4 4 has a left myq now has 5 0==1-1 yes print 4
myq=5 now 5 is popped 5 hs no left and no ryt and 0==1-1 yes so print 5
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        myq=[root]
        result=[]
        while myq!=[]:
            levelsize=len(myq)
            for i in range(levelsize):
                node=myq.pop(0)
                if node.left:
                    myq.append(node.left)
                if node.right:
                    myq.append(node.right)
                if i==levelsize-1:
                    result.append(node.val)
        return result

        