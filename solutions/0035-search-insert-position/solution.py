class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        idx=-1
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                idx=mid
                low=mid+1
            else:
                high=mid-1
        if idx==-1:
            return 0
        return idx+1
        
