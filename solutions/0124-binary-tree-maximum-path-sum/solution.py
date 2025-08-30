# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        # ans=[float('-inf')]
        # findans(root,ans)
        # return ans[0]
        # above given TLE 
        ans=[float('-inf')]
        def f(root):
            if root is None:
                return 0
            lefty=max(0,f(root.left))
            righty=max(f(root.right),0)
            ans[0]=max(ans[0],lefty+righty+root.val)
            return max(lefty,righty)+root.val
        x=f(root)
        return ans[0]


# def singlepathsum(root):
#     if root is None:
#         return 0
#     k=root.val+max(max(singlepathsum(root.left),0),max(singlepathsum(root.right),0))
#     return k

# def findans(root,ans):
#     lefty=max(singlepathsum(root.left),0)
#     righty=max(singlepathsum(root.right),0)
#     ans[0]=max(ans[0],root.val+lefty+righty)
#     if root.left:
#         findans(root.left,ans)
#     if root.right:
#         findans(root.right,ans)





        
