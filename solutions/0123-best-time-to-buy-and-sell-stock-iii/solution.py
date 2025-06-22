class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        return f(prices,0,1,dp,0)
        

def f(prices,i,buy,dp,noof):
    if i==len(prices) or noof==2:
        return 0
    profit=0
    if (i,buy,noof) in dp:
        return dp[(i,buy,noof)]

    if buy:
        x=-prices[i]+f(prices,i+1,0,dp,noof)
        y=f(prices,i+1,1,dp,noof)
        profit=max(x,y)
    else:
        x=prices[i]+f(prices,i+1,1,dp,noof+1)
        y=f(prices,i+1,0,dp,noof)
        profit=max(x,y)
    dp[(i,buy,noof)]=profit
    return profit
