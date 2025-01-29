class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        temp=n
        if n<0:
            n=-1*n
        while n>0:
            if n%2==0:
                n=n//2
                x*=x
            else:
                ans=ans*x
                n-=1
        if temp<0:
            return 1.0/ans
        return ans

        
