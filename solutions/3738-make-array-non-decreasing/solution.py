from itertools import accumulate
from bisect import bisect_left
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n=len(nums)
        idx = 0
        nofsegments = 0

        while idx < n:
            nofsegments += 1
            segment_max = nums[idx]
            j = idx + 1

            while j < n and nums[j] < segment_max:
                segment_max = max(segment_max, nums[j])
                j += 1

            idx = j

        return nofsegments
            
        
                
        
