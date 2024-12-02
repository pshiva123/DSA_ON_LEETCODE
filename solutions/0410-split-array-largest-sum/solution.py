class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(arr,n,mid):
            c=0
            s=0
            for i in range(n):
                if arr[i]+s<=mid:
                    s+=arr[i]
                else:
                    c+=1
                    s=arr[i]
            return c+1
        low=max(nums)
        high=sum(nums)
        while(low<=high):
            mid=(low+high)//2
            if check(nums,len(nums),mid)>k:
                low=mid+1
            else:
                high=mid-1
        return low
        
