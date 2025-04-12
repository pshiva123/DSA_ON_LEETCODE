import math
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        b=math.floor(math.log2(n))+1
        return 1<<b
        
            
       
        
        
        
