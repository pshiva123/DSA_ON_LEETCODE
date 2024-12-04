class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                if s[j] in d:
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                maxi=max(d.values())
                mini=min(d.values())
                #print(maxi,mini)
                ans+=(maxi-mini)
        return ans
        
