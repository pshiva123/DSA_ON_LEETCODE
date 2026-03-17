from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        cost=[[0]*m for i in range(n)]
        return f(grid,vis,n,cost,m)
        
            
def f(arr,vis,n,cost,m):
    queue=deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:
                vis[i][j]=True
                queue.append((i,j))
    di=[(-1,0),(1,0),(0,-1),(0,1)]  
    while queue:
        ob=queue.popleft()
        for d in di:
            nr=d[0]+ob[0]
            nc=d[1]+ob[1]
            if 0<=nr<n and 0<=nc<m:
                if vis[nr][nc]==False and arr[nr][nc]==1:
                    vis[nr][nc]=True
                    cost[nr][nc]=cost[ob[0]][ob[1]]+1
                    arr[nr][nc]=2
                    queue.append((nr,nc))
    notrotten=0
    print(*arr)
    for row in arr:
        for col in row:
            if col==1:
                notrotten=-1
                break
    if notrotten==-1:
        return notrotten
    else:
        maxi=0
        for row in cost:
            for col in row:
                if col>maxi:
                    maxi=col
        return maxi
    
