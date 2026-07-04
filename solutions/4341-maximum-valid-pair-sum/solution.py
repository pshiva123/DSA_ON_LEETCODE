class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxi=float('-inf')
        n=len(nums)
        premax=[]
        premax.append(nums[0])
        for i in range(1,n):
            premax.append(max(premax[-1],nums[i]))
        for i in range(k,n):
            maxi=max(maxi,premax[i-k]+nums[i])
        return maxi
        
