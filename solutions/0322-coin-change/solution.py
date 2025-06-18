class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for i in range(amount+1)] for i in range(len(coins))]
        x=count(coins,amount,len(coins)-1,dp)
        if x==float('inf'):
            return -1
        else:
            return x

def count(arr,amount,idx,dp):
    if idx==0:
        if (amount%arr[0])==0:
            return amount//arr[0]
        return float('inf')
    if dp[idx][amount]!=-1:
        return dp[idx][amount]
    nottake=count(arr,amount,idx-1,dp)
    take=float('inf')
    if amount>=arr[idx]:
            take=1+count(arr,amount-arr[idx],idx,dp)
    dp[idx][amount]=min(take,nottake)
    return dp[idx][amount]




        
