# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import bisect
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([])
        if root is None:
            return 0
        q.append((root,0))
        ans=0
        while q:
            s=len(q)
            first,last=0,0
            for i in range(s):
                nd,idx=q[i][0],q[i][1]
                if i==0:
                    first=idx
                if i==s-1:
                    last=idx
                if nd.left:
                    q.append((nd.left,2*idx+1))
                if nd.right:
                    q.append((nd.right,2*idx+2))
            for _ in range(s):
                q.popleft()
            ans=max(last-first+1,ans)
        return ans


       
            

