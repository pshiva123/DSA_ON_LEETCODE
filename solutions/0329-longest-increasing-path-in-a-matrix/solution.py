class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[-1 for i in range(m)]for j in range(n)]
        ans=1
        for i in range(n):
            for j in range(m):
                x=findroute(matrix,i,j,n,m,dp)
                ans=max(ans,x)
        return ans
di=[(-1,0),(0,-1),(1,0),(0,1)]
def findroute(matrix,x,y,n,m,dp):
    global di
    temp=1
    if dp[x][y]!=-1:
        return dp[x][y]
    for way in di:
        i=way[0]+x
        j=way[1]+y
        if 0<=i<n and 0<=j<m and matrix[i][j]>matrix[x][y]:
            xx=findroute(matrix,i,j,n,m,dp)+1
            temp=max(temp,xx)
    dp[x][y]=temp
    return temp
    

