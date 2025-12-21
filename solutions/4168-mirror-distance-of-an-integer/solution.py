class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp=n
        ans=0
        while temp>0:
            ans=ans*10+temp%10
            temp=temp//10
        #print(ans)
        return abs(ans-n)
        
