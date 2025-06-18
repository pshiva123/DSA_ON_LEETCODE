class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums)-target<0 or (sum(nums)-target)%2==1:
            return 0
        s=(sum(nums)-target)//2
        n=len(nums)
        dp=[[0 for i in range(s+1)] for j in range(n)]
        if nums[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
        if nums[0]!=0 and nums[0]<=s:
            dp[0][nums[0]]=1
        m=int(1e9+7)
        for i in range(1,n):
            for j in range(s+1):
                nt=dp[i-1][j]
                take=0
                if nums[i]<=j:

                    take=dp[i-1][j-nums[i]]

                dp[i][j]=(take+nt)%m

        return dp[n-1][s]
        
        



        
