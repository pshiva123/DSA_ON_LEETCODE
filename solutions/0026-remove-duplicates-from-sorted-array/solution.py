class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i=0
        j=1
        n=len(arr)
        while(i<n and j<n):
            if arr[j]!=arr[i]:
                i+=1
                arr[i]=arr[j]
                j+=1
            else:
                j+=1
        return i+1

        
