class Solution:
    def largestPrime(self, n: int) -> int:
        arr=[True]*(n+1)
        for i in range(2,len(arr)):
            if arr[i] == True:
                j=i*i
                while j<len(arr):
                    arr[j]=False
                    j+=i
        #print(*arr)
        sum1=0
        pointer=2
        ans=float('inf')
        while sum1+pointer<=n and pointer<len(arr):
            if arr[pointer] is True:
                #print(pointer,'ent')
                sum1=sum1+pointer
                if arr[sum1] is True:
                    ans=sum1
            pointer+=1
        
        return ans if ans!=float('inf') else 0


        
