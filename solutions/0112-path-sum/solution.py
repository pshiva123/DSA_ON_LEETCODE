# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def haspath(node,temp,target):
            if node.left is None and node.right is None:
                return temp+node.val
            if node.left:
                x=haspath(node.left,temp+node.val,target)
                if x==target:
                    return x
            if node.right:
                x= haspath(node.right,temp+node.val,target)
                if x==target:
                    return x
            return -1001
                 
        if haspath(root,0,targetSum)==targetSum:
            return True
        return False
            

