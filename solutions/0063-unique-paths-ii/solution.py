class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0 for i in range(m)]for j in range(n)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(1,m):
            if obstacleGrid[0][i]==1:
                dp[0][i]=0
                break
            dp[0][i]=dp[0][i-1]
        for i in range(1,n):
            if obstacleGrid[i][0]==1:
                dp[i][0]=0
                break
            dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
            
        
