class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        arr=[True]*(n+1)
        arr[1]=False
        cnt=0
        for i in range(2,n):
            if arr[i]==True:
                cnt+=1
                for j in range(i*i,n,i):
                    arr[j]=False
        return cnt

