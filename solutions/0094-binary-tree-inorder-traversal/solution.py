# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack=[]
        ans=[]
        node=root
        while True:
            if node:
                stack.append(node)
                node=node.left
            else:
                if stack==[]:
                    break
                x=stack.pop()
                ans.append(x.val)
                node=x.right
        return ans
            
        
