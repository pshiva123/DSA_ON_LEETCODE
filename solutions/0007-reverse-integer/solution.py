class Solution:
    def reverse(self, x: int) -> int:
        negitive=False
        if x<0:
            negitive=True
        x=abs(x)
        rev=0
        while(x>0):
            rev=(rev*10)+(x%10)
            x//=10
        if rev>(2**31)-1:
            return 0
        if negitive:
            return -1*rev
        return rev

        
