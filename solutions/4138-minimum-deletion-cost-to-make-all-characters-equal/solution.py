class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d={}
        n=len(s)
        for i in range(n):
            if s[i] in d:
                d[s[i]]+=cost[i]
            else:
                d[s[i]]=cost[i]
        temp=sum(d.values())
        ans=float('inf')
        for key in d:
            rem=temp-d[key]
            ans=min(ans,rem)
        return ans
        
        
        
