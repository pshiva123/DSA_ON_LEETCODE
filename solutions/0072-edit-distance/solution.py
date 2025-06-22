class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*len(word2) for _ in range(len(word1))]
        return f(word1,word2,0,0,dp)

def f(word1,word2,idx1,idx2,dp):
    if idx1==len(word1):
        return len(word2)-idx2
    if idx2==len(word2):
        return len(word1)-idx1
    if dp[idx1][idx2]!=-1:
        return dp[idx1][idx2]
    temp=0
    if word1[idx1]==word2[idx2]:
        temp=f(word1,word2,idx1+1,idx2+1,dp)
    else:
        replace=1+f(word1,word2,idx1+1,idx2+1,dp)
        delete=1+f(word1,word2,idx1+1,idx2,dp)
        insert=1+f(word1,word2,idx1,idx2+1,dp)
        temp=min(replace,insert,delete)
    dp[idx1][idx2]=temp
    return temp


    
        
