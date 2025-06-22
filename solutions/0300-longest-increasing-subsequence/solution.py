class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        li=[]
        maxi=1
        n=len(arr)
        li.append(arr[0])
        for i in range(1,n):
            if arr[i]>li[-1]:
                li.append(arr[i])
            else:
                idx=bs(li,arr[i],0,len(li))
                li[idx]=arr[i]
            maxi=max(maxi,len(li))
        return (maxi)

def bs(arr,ele,low,high):
    idx=-1
    while (low<=high):
        mid=(low+high)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            idx=mid
            high=mid-1
        else:
            low=mid+1
    return idx
        
