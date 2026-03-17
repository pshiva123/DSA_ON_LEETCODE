class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        x=0
        for i in s1:
            xx=ord(i)-97
            x+=37**xx
        n=len(s1)
        ff2=0
        for i in range(n):
            ff2+=37**(ord(s2[i])-97)
        if ff2==x:
            return True
        for i in range(n,len(s2)):
            ff2-=37**(ord(s2[i-n])-97)
            ff2+=37**(ord(s2[i])-97)
            if ff2==x:
                return True
        return False


        
