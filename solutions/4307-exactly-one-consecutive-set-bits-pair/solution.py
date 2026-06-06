class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        s=bin(n)[2:]
        c=0
        for i in range(len(s)-1):
            if s[i]==s[i+1] and s[i]=="1":
                c+=1
        return True if c==1 else False
