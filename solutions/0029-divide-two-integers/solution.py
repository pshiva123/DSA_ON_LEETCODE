class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        sign=True
        if(dividend>=0 and divisor<0) or (dividend<0 and divisor>0):
            sign=False
        n=abs(dividend)
        a=abs(divisor)
        if n==a:
            return -1
        ans=0
        while(n>=a):
            cnt=0
            while(n>=(a<<(cnt+1))):
                cnt+=1
            ans+=1<<cnt
            n=n-(1<<cnt)*a
        if ans>=2**31 and sign:
            return 2**31-1
        if ans<-1*2**31 and not sign:
            return -2**31
        return ans if sign else -ans

        
