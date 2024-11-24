class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        ans=float('inf')
        for i in range(l,r+1):
            for j in range(0,n-i+1):
                s=sum(nums[j:j+i])
                if s>0:
                    ans=min(ans,s)
        if ans==float('inf'):
            ans=-1
        return ans
                
            
            
        
        
