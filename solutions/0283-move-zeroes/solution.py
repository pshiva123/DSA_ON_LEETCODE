class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=-1
        for i in range(0,len(arr)):
            if arr[i]==0:
                j=i
                break
        if j==-1:
            return 
            
        n=len(arr)
        for i in range(j+1,n):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1

             
            
            
        
