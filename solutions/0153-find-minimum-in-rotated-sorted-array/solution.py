class Solution:
    def findMin(self, arr: List[int]) -> int:
        h=len(arr)-1
        l=0
        ans=float('inf')
        while(l<=h):
            m=(l+h)//2
            if arr[m]<=arr[h]:
                ans=min(ans,arr[m])
                h=m-1
            else:
                ans=min(ans,arr[l])
                l=m+1
        return ans


        
