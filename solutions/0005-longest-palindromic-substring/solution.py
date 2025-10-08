class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=1
        ansstr=s[0]
        n=len(s)
        for i in range(n):
            p1=i
            p2=i
            while p1>=0 and p2<n and s[p1]==s[p2]:
                if(ans<p2-p1+1):
                    ansstr=s[p1:p2+1]
                    ans=p2-p1+1
                p1-=1
                p2+=1
            p1=i
            p2=i+1
            while p1>=0 and p2<n and s[p1]==s[p2]:
                if(ans<p2-p1+1):
                    ansstr=s[p1:p2+1]
                    ans=p2-p1+1
                p1-=1
                p2+=1       
        return ansstr   
