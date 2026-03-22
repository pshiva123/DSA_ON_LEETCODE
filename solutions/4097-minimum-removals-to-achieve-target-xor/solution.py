class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n=len(nums)
        x=f(0,n,nums,0,target,{})
        if x<0:
            return -1
        return n-x



def f(idx,n,arr,xr,target,dp):
    if idx==n:
        if xr==target:
            return 0
        return -10**9
        
    if (idx,xr) in dp:
        return dp[(idx,xr)]
        
    nottake=f(idx+1,n,arr,xr,target,dp)
    take=1+f(idx+1,n,arr,xr^arr[idx],target,dp)
    
    dp[(idx,xr)]=max(nottake,take)
    
    return max(nottake,take)
    
        

