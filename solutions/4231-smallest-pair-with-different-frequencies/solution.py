from collections import Counter
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d=Counter(nums)
        n=len(nums)
        x,y=float('inf'),float('inf')
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]<nums[j] and d[nums[i]]!=d[nums[j]]:
                    if nums[i]<x:
                        x=nums[i]
                        y=nums[j]
                    elif nums[i]==x:
                        y=min(nums[j],y)
        if x==float('inf'):
            return [-1,-1]
        return [x,y]
                    
        
        
        
