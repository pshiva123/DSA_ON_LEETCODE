# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def f(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        lefty=self.f(root.left)
        righty=self.f(root.right)
        dia=lefty+righty+1
        self.ans=max(self.ans,dia)
        return max(lefty,righty)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        temp=self.f(root)
        return self.ans-1
        






        
