class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        s1=0
        s2=1
        while(temp>0):
            s1+=temp%10
            s2=s2*(temp%10)
            temp=temp//10
        return s2-s1
        
        
