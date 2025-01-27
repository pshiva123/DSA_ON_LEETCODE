# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([])
        if root is None:
            return[]
        li=[]
        queue.append(root)
        queue.append(None)
        arr=[]
        while queue:
            curr=queue.popleft()
            if curr is None:
                if arr:
                    li.append(arr)
                    arr=[]
                if queue:
                    queue.append(None)
            else:
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return li

        
