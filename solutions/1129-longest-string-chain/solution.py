class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n=len(words)
        words=sorted(words,key=len)
        dp=[1]*n
        ans=1
        for i in range(1,n):
            for j in range(i):
                if compare(words[i],words[j]) and dp[i] < dp[j]+1:
                    dp[i]=dp[j]+1
            ans=max(ans,dp[i])
        return ans

def compare(s1,s2):
    if len(s1)!=len(s2)+1:
        return False
    n=len(s1)
    m=len(s2)
    i,j=0,0
    cnt=0
    while(i<n and j<m):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            i+=1
            cnt+=1
        if cnt>1:
            return False
    return s1[i+1:]==s2[j+1:]
    

        
