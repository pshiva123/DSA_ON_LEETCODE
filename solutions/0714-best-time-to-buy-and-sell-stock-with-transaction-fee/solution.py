class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp={}
        return f(prices,0,1,dp,fee)

def f(prices,i,buy,dp,fee):
    if i>=len(prices):
        return 0
    if (i,buy) in dp:
        return dp[(i,buy)]
    profit=0
    if buy:
        x=-prices[i]+f(prices,i+1,0,dp,fee)
        y=f(prices,i+1,1,dp,fee)
        profit=max(x,y)
    else:
        x=prices[i]+f(prices,i+1,1,dp,fee)-fee
        y=f(prices,i+1,0,dp,fee)
        profit=max(x,y)
    dp[(i,buy)]=profit
    return profit
        
