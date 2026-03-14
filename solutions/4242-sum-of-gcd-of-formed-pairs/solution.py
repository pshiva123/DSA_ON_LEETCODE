from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            maxi.append(max(maxi[-1],nums[i]))
        prefix=[]
        #print(maxi)
        for i in range(n):
            prefix.append(gcd(maxi[i],nums[i]))
        prefix.sort()
        i=0
        j=len(prefix)-1
        s=0
        #print(prefix)
        while i<j:
            x=gcd(prefix[i],prefix[j])
            i+=1
            j-=1
            s+=x
        return s
            
        
        
