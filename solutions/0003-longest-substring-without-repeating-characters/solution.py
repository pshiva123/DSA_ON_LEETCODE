class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        d={}
        maxi=1
        idx=-1
        for i in range(len(s)):
            if s[i] in d:
                maxi=max(i-1-idx,maxi)
                temp=d[s[i]]
                for j in range(idx+1,temp+1):
                    del d[s[j]]

                idx=temp
                d[s[i]]=i
            else:
                d[s[i]]=i
        return max(len(d),maxi)
        
            
            
                
        
