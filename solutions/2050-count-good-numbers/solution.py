class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x=ceil(n//2)+(n%2)
        y=floor(n//2)
        print(x,y)
        return int(power(5,x)*power(4,y))%1000000007
def power(a,b):
    ans=1
    m=1000000007
    while(b>0):
        if b%2==1:
            ans=(ans*a)%m
        a=(a*a)%m
        b=b>>1
    return ans





