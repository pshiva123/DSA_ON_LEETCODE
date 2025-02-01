class Solution:
    def findValidPair(self, s: str) -> str:
        c=Counter(s)
        for i in range(0,len(s)-1):
            if(s[i]!=s[i+1]):
                if c[s[i]]==int(s[i]) and c[s[i+1]]==int(s[i+1]):
                    return s[i:i+2]
        return ""
        
