# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        li=[]
        stack=[root]
        while stack:
            x=stack.pop()
            li.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        return li

            

        
