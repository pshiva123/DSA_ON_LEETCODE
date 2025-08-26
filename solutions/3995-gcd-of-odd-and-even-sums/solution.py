class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a,b=0,0
        for i in range(1,2*n+1):
            if i&1:
                b+=i
            else:
                a+=i
        while(b>0):
            if a>b:
                a=a-b
            else:
                b=b-a
        return a
            
        
