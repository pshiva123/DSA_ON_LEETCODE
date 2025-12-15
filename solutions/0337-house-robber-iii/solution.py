# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(f(root,0,{}),f(root,1,{}))

def f(node,taken,dp):
    if node== None:
        return 0
    if (node,taken) in dp:
        return dp[(node,taken)]
    if taken==1:
        dp[(node,taken)]=node.val+f(node.left,0,dp)+f(node.right,0,dp)
        return dp[(node,taken)]
    dp[(node,taken)]=max(f(node.left,1,dp),f(node.left,0,dp))+max(f(node.right,1,dp),f(node.right,0,dp))
    return dp[(node,taken)]

    
    

    
        
