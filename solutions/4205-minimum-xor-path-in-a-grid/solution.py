from collections import deque
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        maxi=1024
        vis=[[[False]*maxi for i in range(m)] for j in range(n)]
        queue=deque()
        start=grid[0][0]
        queue.append((0,0,start))
        mini=float('inf')
        vis[0][0][start]=True
        while queue:
            i,j,xor=queue.popleft()
            if i==n-1 and j==m-1:
                mini=min(mini,xor)
                continue
            if i+1<n:
                newxor=grid[i+1][j]^xor
                if vis[i+1][j][newxor]==False:
                    vis[i+1][j][newxor]=True
                    queue.append((i+1,j,newxor))
            if j+1<m:
                newxor=grid[i][j+1]^xor
                if vis[i][j+1][newxor]==False:
                    vis[i][j+1][newxor]=True
                    queue.append((i,j+1,newxor))
        return mini

        
                
            

    
        




            
        
            
        
