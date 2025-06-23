class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        dp=[[-1]*len(nums) for _ in range(len(nums))]
        return f(nums,1,len(nums)-1,dp)
        

def f(nums,i,j,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    maxi=-1*float('inf')
    for k in range(i,j):
        coins=nums[i-1]*nums[k]*nums[j]+f(nums,i,k,dp)+f(nums,k+1,j,dp)
        maxi=max(maxi,coins)
    dp[i][j]=maxi
    return maxi



    
            


