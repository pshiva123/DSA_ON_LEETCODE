import math
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        m=int(1e9+7)
        cur=k
        ans=0
        a=1
        for i in nums:
            if i<=cur:
                cur=cur-i
            else:
                t=(i-cur+k-1)//k
                ans=(ans+t*(2*a+t-1)//2)%m
                cur+=t*k
                a+=t
                cur=cur-i
        return ans%m
                
                
                
            
        
