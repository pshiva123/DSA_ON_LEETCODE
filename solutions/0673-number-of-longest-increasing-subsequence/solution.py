class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[1]*n
        maxi=1
        cnt=[1]*n
        for i in range(1,n):
            for j in range(i):
                if arr[i]>arr[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    cnt[i]=cnt[j]
                elif arr[i]>arr[j] and dp[i]==dp[j]+1:
                    cnt[i]+=cnt[j]
            maxi=max(dp[i],maxi)
        
        no=0
        for i in range(len(dp)):
            if dp[i]==maxi:
                no+=cnt[i]
        return no


        
            
        
    

        
