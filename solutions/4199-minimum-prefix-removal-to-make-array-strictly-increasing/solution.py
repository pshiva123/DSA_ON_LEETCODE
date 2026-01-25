class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        idx=0
        n=len(nums)
        if n==1:
            return 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                continue
            return i+1
        return 0
        
            
        
