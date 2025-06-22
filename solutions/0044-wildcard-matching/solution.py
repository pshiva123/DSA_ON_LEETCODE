class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1]*len(p) for _ in range(len(s))]
        return f(s,p,0,0,dp)==1
    

def f(s, p, i, j,dp):
    # 1) If we've consumed the entire pattern...
    if j == len(p):
        # we match if and only if we've also consumed the entire string
        return i == len(s)

    # 2) If we've consumed the entire string...
    if i == len(s):
        # we match only if the remaining pattern are all '*' (they can match empty)
        return all(ch == '*' for ch in p[j:])
    if dp[i][j]!=-1:
        return dp[i][j]

    # 3) Otherwise, handle current character/pattern:
    ans=-1
    if p[j] == '?' or s[i] == p[j]:
        ans=f(s, p, i+1, j+1,dp)
    elif p[j] == '*':
        # '*' can match empty (advance pattern) or match one char (advance string)
        ans= f(s, p, i,   j+1,dp) \
            or f(s, p, i+1, j,dp)
    else:
        ans=0
    dp[i][j]=ans
    return ans

        
