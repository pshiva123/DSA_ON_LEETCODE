class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if  not set(text1).intersection(set(text2)):
            return 0
        dp=[[-1 for j in range(len(text2))]for i in range(len(text1))]
        return f(text1,text2,0,0,dp)
    
def f(text1,text2,i,j,dp):
    if i==len(text1) or j==len(text2):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    ans=0
    if text1[i]==text2[j]:
        ans=1+f(text1,text2,i+1,j+1,dp)
    else:
        x=f(text1,text2,i+1,j,dp)
        y=f(text1,text2,i,j+1,dp)
        ans=max(x,y)
    dp[i][j]=ans
    return ans
        
