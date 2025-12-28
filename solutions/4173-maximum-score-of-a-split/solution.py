class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            prefix.append(nums[i]+prefix[-1])
        suffix=[0]*n
        suffix[-1]=float('inf')
        for i in range(n-2,-1,-1):
            suffix[i]=min(nums[i+1],suffix[i+1])
        ans=float('-inf')
        for i in range(n):
            ans=max(ans,prefix[i]-suffix[i])
        return ans
        
        
