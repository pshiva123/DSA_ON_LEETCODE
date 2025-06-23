class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m=len(cuts)
        cuts.sort()
        cuts.append(n)
        cuts=[0]+cuts
        dp=[[-1]*(m+1) for _ in range(m+1)]
        return f(cuts,1,m,dp)
        


def f(cuts,i,j,dp):
    if i>j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    mini=float('inf')
    for k in range(i,j+1):
        cost=cuts[j+1]-cuts[i-1]+f(cuts,i,k-1,dp)+f(cuts,k+1,j,dp)
        mini=min(cost,mini)
    dp[i][j]=mini
    return mini

        
