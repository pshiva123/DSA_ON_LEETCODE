class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans=""
        cnt=0
        for i in range(len(s)):
            if s[i]!=x and s[i]!=y:
                ans+=s[i]
            elif s[i]==y:
                ans+=s[i]
            else:
                cnt+=1
        for i in range(cnt):
            ans+=x
        return ans
        
