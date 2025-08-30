# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return f(p,q)

    
def f(p,q):
    if p is None and q is None:
        return True
    if (p is None and q is not None) or (p is not None and q is None):
        return False
    if p.val!=q.val:
        return False
    if p.left is None and p.right is None and q.left is None and q.right is None:
        return p.val==q.val
    x=f(p.left,q.left)
    y=f(p.right,q.right)
    return x and y
        
