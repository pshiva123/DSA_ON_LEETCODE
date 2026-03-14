class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0 and nums.count(nums[i])==1:
                return nums[i]
        return -1
        
        
                
        
        
        
