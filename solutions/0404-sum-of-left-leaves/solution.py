# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        d={}
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left is not None:
                q.append(node.left)
                d[node.left]="left"
            if node.right is not None:
                q.append(node.right)
                d[node.right]="right"
        def f(root,d):
            if root is None:
                return 0
            if root.left is None and root.right is None and d[root]=='left':
                return root.val
            a=f(root.left,d)
            b=f(root.right,d)
            return a+b
        return f(root,d)
                
            
        
        
