# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag=True
    def f(self,root):
        if root.left is None and root.right is None:
            return 0
        lefty,righty=0,0
        if root.left:
            lefty=1+self.f(root.left)
        if root.right:
            righty=1+self.f(root.right)
        if abs(lefty-righty)>1:
            self.flag=False
        return max(lefty,righty)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        temp=self.f(root)
        return self.flag





        
