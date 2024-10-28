class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(arr)
        k=len(arr)-k
        i=0
        j=k-1
        while(i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        i=k
        j=len(arr)-1
        while(i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        i=0
        j=len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
