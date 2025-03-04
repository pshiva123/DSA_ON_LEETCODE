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
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=Trie()
        maxi=0
        for i in nums:
            root.insert(i)
            maxi=max(maxi,root.findxor(i))
        return maxi
        
