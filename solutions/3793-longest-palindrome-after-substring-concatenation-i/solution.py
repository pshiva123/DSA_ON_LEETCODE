class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans=1
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                for k in range(len(t)):
                    for l in range(k,len(t)):
                        x=temp+t[k:l+1]
                        if x==x[::-1]:
                            #print(x)
                            ans=max(ans,len(x))
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=s[i:j+1] 
                if temp==temp[::-1]:
                    ans=max(ans,len(temp))
        for i in range(len(t)):
            for j in range(i,len(t)):
                temp=t[i:j+1] 
                if temp==temp[::-1]:
                    ans=max(ans,len(temp))
        return ans
        
