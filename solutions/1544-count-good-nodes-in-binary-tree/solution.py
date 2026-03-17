# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return fun(root,root.val)

    

def fun(node,maxi):
    if not node:
        return 0
    #print(node.val,maxi)
    if node.val>=maxi:
        return 1+fun(node.left,node.val)+fun(node.right,node.val)
    return fun(node.left,maxi)+fun(node.right,maxi)
