# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def trim(root,low,high):
            if root is None:
                return root
            if root.val<low:
                return trim(root.right,low,high)
            if root.val>high:
                return trim(root.left,low,high)
            root.left=trim(root.left,low,high)
            root.right=trim(root.right,low,high)
            return root
        return trim(root,low,high)
        
        
        
        
