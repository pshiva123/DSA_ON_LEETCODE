class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x%2==0 for x in nums1):
            return True
        m=min(nums1)
        return m%2==1
        
