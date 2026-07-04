class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        x=nums[len(nums)//2]
        return True if nums.count(x)==1 else False
        
