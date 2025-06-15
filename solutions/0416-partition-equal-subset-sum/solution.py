class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        dp={}
        return f(len(nums)-1,sum(nums)//2,nums,dp)
def f(idx,cur,arr,dp):
    if idx<0:
        if cur==0:
            return True
        else:
            return False
    if (idx,cur) in dp:
        return dp[(idx,cur)]
    if cur==0:
        return True
    temp=f(idx-1,cur-arr[idx],arr,dp) or f(idx-1,cur,arr,dp)
    dp[(idx,cur)]=temp
    return temp
