class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        d={}
        ans=s[0]
        d[s[0]]=0
        n=len(s)
        removed=0
        for i in range(1,n):
            if s[i] in d:
                if i-d[s[i]]-removed<=k:
                    removed+=1
                else:
                    ans+=s[i]
                    d[s[i]]=i-removed
            else:
                ans+=s[i]
                d[s[i]]=i-removed
        return ans
