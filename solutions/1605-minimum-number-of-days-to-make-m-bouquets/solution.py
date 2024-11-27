class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if possible(bloomDay,m,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



def possible(arr,m,k,day):
    cnt=0
    noofboque=0
    for i in arr:
        if i<=day:
            cnt+=1
        else:
            noofboque+=cnt//k
            cnt=0
    noofboque+=cnt//k
    return noofboque>=m
