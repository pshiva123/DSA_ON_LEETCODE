class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        a=0
        b=1
        c=2
        for i in range(2,n+1):
            a,b=b,a+b
        return b
        
