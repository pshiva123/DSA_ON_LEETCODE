class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mini=float('inf')
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]==1 and nums[j]==2) or (nums[i]==2 and nums[j]==1):
                    mini=min(mini,abs(i-j))
        return mini if mini!=float('inf') else -1
                
        
