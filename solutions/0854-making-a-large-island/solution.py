class disjointset:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    def findpar(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.findpar(self.parent[u])
        return self.parent[u]
    def unionbysize(self,u,v):
        uup=self.findpar(u)
        vup=self.findpar(v)
        if uup==vup:
            return
        
        if self.size[uup]>self.size[vup]:
            self.size[uup]+=self.size[vup]
            self.parent[vup]=uup
        else:
            self.size[vup]+=self.size[uup]
            self.parent[uup]=vup
    
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dj=disjointset(m*n)
        d=[(-1,0),(1,0),(0,1),(0,-1)]
        for row in range(n):
            for col in range(m):
                if grid[row][col]==1:
                    x=row*m+col
                    for i,j in d:
                        nr,nc=i+row,j+col
                        if 0<=nr<n and 0<=nc<m:
                            if grid[nr][nc]==1:
                                y=nr*m+nc
                                dj.unionbysize(x,y)
        ans=max(dj.size)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    temp=1
                    comp=set()
                    for k,l in d:
                        nr,nc=i+k,j+l
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                            comp.add(dj.findpar(nr*m+nc))
                    for island in comp:
                        temp+=dj.size[island]
                            
                    ans=max(ans,temp)
        return ans

            
        
