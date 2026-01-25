from collections import deque
            
        
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph=[[] for i in  range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(src):
            dis=[-1]*n
            dis[src]=0
            q=deque([])
            q.append(src)
            while q:
                node=q.popleft()
                for neigh in graph[node]:
                    if dis[neigh]>dis[node]+1 or dis[neigh]==-1:
                        dis[neigh]=dis[node]+1
                        q.append(neigh)
            return dis
        dx=bfs(x)
        dy=bfs(y)
        dz=bfs(z)
        cnt=0
        for i in range(n):
            a,b,c=sorted([dx[i],dy[i],dz[i]])
            if a*a+b*b==c*c:
                cnt+=1
        return cnt
        
        
