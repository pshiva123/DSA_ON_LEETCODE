class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysss(wts,capacity):
            curr=0
            n=1
            for i in wts:
                if curr+i>capacity:
                    n+=1
                    curr=i
                else:
                    curr+=i
            return n
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            n=daysss(weights,mid)
            if n<=days:
                high=mid-1
            else:
                low=mid+1
        return low

        
