class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[-1]*(amount+1) for j in range(len(coins))]
        return f(amount,len(coins)-1,coins,dp)

def f(target,idx,arr,dp):
    #print(target,idx,"arr")
    if target==0:
        return 1
    if target<0:
        return 0
    if idx==0:
        return int(target%arr[idx]==0)
    if dp[idx][target]!=-1:
        return dp[idx][target]
    take=f(target-arr[idx],idx,arr,dp)
    nottake=f(target,idx-1,arr,dp)

    dp[idx][target]=take + nottake
    return dp[idx][target]
        
