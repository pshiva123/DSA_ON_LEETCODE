class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        return f(s,t,0,0,dp)


def f(s,t,idx1,idx2,dp):
    if idx2==len(t):
        return 1
    if idx1==len(s):
        return 0
    if dp[idx1][idx2]!=-1:
        return dp[idx1][idx2]
    ans=0
    if s[idx1]==t[idx2]:
        ans=f(s,t,idx1+1,idx2+1,dp)+f(s,t,idx1+1,idx2,dp)
    else:
        ans=f(s,t,idx1+1,idx2,dp)
    #x=take+nottake

    dp[idx1][idx2]=ans
    return ans
