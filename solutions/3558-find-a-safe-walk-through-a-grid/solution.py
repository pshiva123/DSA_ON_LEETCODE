class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        movements=[(0,1),(1,0),(0,-1),(-1,0)]
        queue=collections.deque([(0,0,health-grid[0][0])])
        visited=[[-1]*n for _ in range(m)]
        visited[0][0]=health-grid[0][0]
        while queue:
            r,c,heal=queue.popleft()
            if r==m-1 and c==n-1 and heal>0:
                return True
            for row,col in movements:
                nr,nc=r+row,c+col
                if (nr>=0 and nr<m) and (nc>=0 and nc<n):
                    newheal=heal-grid[nr][nc]
                    if newheal>0 and newheal>visited[nr][nc]:
                        visited[nr][nc]=newheal
                        queue.append((nr,nc,newheal))
        return False

        
