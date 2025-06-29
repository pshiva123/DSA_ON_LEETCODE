# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], valu: int) -> Optional[TreeNode]:
        while root!=None:
            if root.val==valu:
                return root
            elif root.val<valu:
                root=root.right
            else:
                root=root.left
        return root
        
