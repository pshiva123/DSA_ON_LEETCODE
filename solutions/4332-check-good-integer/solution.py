class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        number=str(n)
        ds,ss=0,0
        for x in number:
            a=int(x)
            ds+=a
            ss+=(a*a)
        return True if ss-ds>=50 else False
