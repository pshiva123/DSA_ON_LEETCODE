class Solution:
    def minCost(self, n: int) -> int:
        ans=0
        while n>0:
            ans+=n-1
            n=n-1
        return ans
        
