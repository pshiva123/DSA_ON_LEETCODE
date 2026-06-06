class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=[0]
        right=[0]
        n=len(nums)
        for i in range(1,n):
            left.append(left[-1]+nums[i-1])
        for i in range(n-2,-1,-1):
            right.append(right[-1]+nums[i+1])
        right.reverse()
        ans=[abs(left[i]-right[i]) for i in range(n)]
        return ans
        
        
        
