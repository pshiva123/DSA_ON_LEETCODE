class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        ans=-1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            k=requiredTime(piles,mid)
            if k<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
def requiredTime(arr,num):
    t=0
    for i in arr:
        t+=math.ceil(i/num)
    return t

        
