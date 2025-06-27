import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        heap=[]
        heapq.heappush(heap,(1,0,0))
        n=len(grid)
        m=len(grid[0])
        dir=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        dis=[[float('inf')]*m for _ in range(n)]
        dis[0][0]=1
        while heap:
            w,i,j=heapq.heappop(heap)
            for d in dir:
                nr,nc=i+d[0],j+d[1]
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0:
                    if dis[nr][nc]>w+1:
                        dis[nr][nc]=w+1
                        heapq.heappush(heap,(dis[nr][nc],nr,nc))

        return -1 if dis[-1][-1]==float('inf') else dis[-1][-1]



        
