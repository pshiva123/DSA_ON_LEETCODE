class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l=1
        h=sum(nums)
        ans=-1
        while l<=h:
            m=(l+h)//2
            if f(nums,m):
                ans=m
                h=m-1
            else:
                l=m+1
        return ans

def f(arr,k):
    op=0
    x=k*k
    for i in arr:
        op+=(i+k-1)//k
        if op>x:
            return False
    return op<=x
                
        
