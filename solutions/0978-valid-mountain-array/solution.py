class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        nums=arr
        if n<3:
            return False
        idx=nums.index(max(nums))
        for i in range(1,idx):
            if nums[i]<=nums[i-1]:
                return False
        for i in range(idx+1,n):
            if nums[i-1]<=nums[i]:
                return False
        if idx==n-1 or idx==0:
            return False 
        return True
