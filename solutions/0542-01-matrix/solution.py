from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        cost=[[float('inf')]*m for _ in range(n)]
        queue=deque([])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append((i,j))
                    cost[i][j]=0
        di=[(-1,0),(0,-1),(1,0),(0,1)]
        while queue:
            x=queue.popleft()
            for d in di:
                nr,nc=d[0]+x[0],d[1]+x[1]
                if 0<=nr<n and 0<=nc<m and mat[nr][nc]!=0:
                    if cost[nr][nc]>cost[x[0]][x[1]]+1:
                        cost[nr][nc]=cost[x[0]][x[1]]+1
                        queue.append((nr,nc))
        return cost





        
