class Solution:
    def maxArea(self, arr: List[int]) -> int:
        n=len(arr)
        i=0
        j=n-1
        ans=0
        while(i<=j):
            k=min(arr[i],arr[j])
            curr=(j-i)*k
            ans=max(ans,curr)
            if k==arr[i]:
                i+=1
            else:
                j-=1
        return ans
