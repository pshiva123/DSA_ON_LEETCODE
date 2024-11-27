class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans=-1
        low=1
        high=max(nums)
        while(low<=high):
            mid=(low+high)//2
            if sumofele(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
def sumofele(nums,mid):
    s=0
    for i in nums:
        s+=math.ceil(i/mid)
    return s
        
