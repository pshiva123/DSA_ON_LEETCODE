class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign=True
        if n<0:
            sign=False
        ans=1
        n=abs(n)
        while(n>0):
            if n%2==1:
                ans=ans*x
                n=n-1
            else:
                x*=x
                n=n//2
        if sign:
            return ans
        return 1/ans
        
