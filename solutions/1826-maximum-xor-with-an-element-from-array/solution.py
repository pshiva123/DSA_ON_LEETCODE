from collections import deque
class Node:
    def __init__(self):
        self.child=[None]*2
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,num):
        cur=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if cur.child[bit] is None:
                cur.child[bit]=Node()
            cur=cur.child[bit]
    def findxor(self,num):
        cur=self.root
        ans=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if cur.child[bit^1]:
                ans=ans|(1<<i)
                cur=cur.child[bit^1]
            else:
                cur=cur.child[bit]
        return ans
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[-1]*len(queries)
        root=Trie()
        nums.sort()
        nums=deque(nums)
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x:x[1])
        for i in range(len(queries)):
            while(nums and nums[0]<=queries[i][1]):
                root.insert(nums[0])
                nums.popleft()
            if root.root.child == [None,None]:
                continue
            temp=root.findxor(queries[i][0])
            ans[queries[i][2]]=temp
        return ans
        



























      
        


        
