class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==2:
            return min(cost)
        for i in range(2,n):
            a=cost[i-1]
            b=cost[i-2]
            cost[i]+=min(a,b)
        return min(cost[n-2:])
