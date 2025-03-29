class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[]
        for i in range(n):
            li=[]
            for j in range(m):
                tempo=[-1 for i in range(32)]
                li.append(tempo)
            dp.append(li)

        x=findxor(grid,0,0,n,m,k,0,dp)
        return x%int(1e9+7)
def findxor(grid,i,j,n,m,k,curxor,dp):
    if i==n-1 and j==m-1 and grid[i][j]^curxor==k:
        return 1
    if i>=n or j>=m:
        return 0
    if dp[i][j][curxor]!=-1:
        return dp[i][j][curxor]
    a1=findxor(grid,i,j+1,n,m,k,curxor^grid[i][j],dp)
    a2=findxor(grid,i+1,j,n,m,k,curxor^grid[i][j],dp)
    dp[i][j][curxor]=(a1+a2)%int(1e9+7)
    return (a1+a2)%int(1e9+7)
        
            

        
