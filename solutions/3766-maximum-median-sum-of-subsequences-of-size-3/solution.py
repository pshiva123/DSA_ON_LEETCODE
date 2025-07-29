class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n
        ans=0
        while(i<j):
            j-=2
            i+=1
            ans+=nums[j]
        return ans
            
            
        
