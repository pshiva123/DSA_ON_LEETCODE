class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        temp=x
        while(temp>0):
            s+=temp%10
            temp=temp//10
        if x%s==0:
            return s
        return -1
        
