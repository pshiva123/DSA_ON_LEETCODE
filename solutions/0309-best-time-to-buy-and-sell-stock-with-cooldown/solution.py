class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        return f(prices,0,1,dp)

def f(prices,i,buy,dp):
    if i>=len(prices):
        return 0
    if (i,buy) in dp:
        return dp[(i,buy)]
    profit=0
    if buy:
        x=-prices[i]+f(prices,i+1,0,dp)
        y=f(prices,i+1,1,dp)
        profit=max(x,y)
    else:
        x=prices[i]+f(prices,i+2,1,dp)
        y=f(prices,i+1,0,dp)
        profit=max(x,y)
    dp[(i,buy)]=profit
    return profit

