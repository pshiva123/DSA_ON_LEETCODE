class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        total=len(nums)
        n=total//2
        a1=nums[:n]
        a2=nums[n:]
        left=[[] for i in range(n+1)]
        right=[[] for i in range(n+1)]
        f(a1,left)
        f(a2,right)
        mini=float('inf')
        for i in range(n+1):
            right[i].sort()
        for i in range(n+1):
            l1=left[i]
            l2=right[n-i]
            for k in l1:
                low=0
                high=len(l2)-1
                find=(totalsum//2)-k
                floor1=findfloor(l2,find)
                ceil1=findceil(l2,find)
                if 0<=floor1<len(l2):
                    mini=min(mini,abs(totalsum-2*(k+l2[floor1])))
                if 0<=ceil1<len(l2):
                    mini=min(mini,abs(totalsum-2*(k+l2[floor1])))
        return mini


def findfloor(arr,k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return high

def findceil(arr,k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return low if low<len(arr) else -1

    

def f(arr,li):
    n=len(arr)
    for i in range(2**n):
        s=0
        sz=0
        idx=0
        while(i>0):
            if i&1:
                s+=arr[idx]
                sz+=1
            idx+=1
            i=i>>1
        li[sz].append(s)
    return li





