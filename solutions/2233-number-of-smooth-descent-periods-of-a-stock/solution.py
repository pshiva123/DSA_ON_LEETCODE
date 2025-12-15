class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        li=[]
        li.append(0)
        ans=1
        i=0
        j=1
        n=len(prices)
        while i<n and j<n:
            if prices[j]-prices[j-1]==-1:
                a=j-i+1
                ans+=a
                j+=1
            else:
                ans+=1
                i=j
                j=i+1
        return ans
            

        
