# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans=0
        def cntdom(root):
            nonlocal ans
            if root.left is None and root.right is None:
                ans+=1
                return root.val
            if root.left and root.right:
                maxi=cntdom(root.left)
                maxi2=cntdom(root.right)
                if root.val>=maxi and root.val>=maxi2:
                    ans+=1
                    return root.val
                return max(maxi,maxi2)
            if root.left:
                maxi=cntdom(root.left)
                if root.val>=maxi:
                    ans+=1
                    return root.val
                return maxi
            if root.right:
                maxi=cntdom(root.right)
                if root.val>=maxi:
                    ans+=1
                    return root.val
                return maxi
        x=cntdom(root)
        return ans