class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        c=1
        for i in range(len(s)):
            if(s[i]==" "):
                c+=1
                if(c==k+1):
                    print(c)
                    return s[:i]
        return s   
        
