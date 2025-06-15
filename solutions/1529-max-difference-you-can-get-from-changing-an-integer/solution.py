from collections import Counter
class Solution:
    def maxDiff(self, num: int) -> int:
        s=str(num)
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                li=[i]
                d[s[i]]=li
        maxi=0
        mini=float('inf')
        for strnum in d:
            for j in range(10):
                ans=[""]*len(s)
                for k in range(len(s)):
                    ans[k]=s[k]
                for x in d[strnum]:
                    ans[x]=str(j)
                ans=''.join(ans)
                if ans[0]=="0":
                    continue
                maxi=max(maxi,int(ans))
        for strnum in d:
            for j in range(10):
                ans=[""]*len(s)
                for k in range(len(s)):
                    ans[k]=s[k]
                for x in d[strnum]:
                    ans[x]=str(j)
                ans=''.join(ans)
                if ans[0]=="0":
                    continue
                mini=min(mini,int(ans))
        return maxi-mini
            
                
                

       
               
