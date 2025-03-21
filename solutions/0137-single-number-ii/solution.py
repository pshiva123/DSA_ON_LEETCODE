import math

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(31,-1,-1):
            temp=0
            for num in nums:
                temp+=1 if (num>>i)&1 else 0
            if temp%3!=0:
                ans=ans|(1<<i)
        if ans>=(1<<31):
            ans-=(1<<32)
        return ans

        
