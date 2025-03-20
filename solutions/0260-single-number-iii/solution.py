from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for i in nums:
            x=x^i
        diff=x & -x
        a,b=0,0
        for i in nums:
            if diff&i:
                a=a^i
            else:
                b=b^i
        return [a,b]
        
        
        
