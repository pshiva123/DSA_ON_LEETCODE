from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=[[] for i in range(n)]
        for f in flights:
            u,v,w=f[0],f[1],f[2]
            graph[u].append([v,w])
        dis=[float('inf')]*n
        queue=deque([])
        queue.append((0,src,0))
        while queue:
            stops,node,cost=queue.popleft()
            for neigh,weight in graph[node]:
                if dis[neigh]>cost+weight and stops<=k:
                    dis[neigh]=cost+weight
                    queue.append((stops+1,neigh,dis[neigh]))
        return -1 if dis[dst]==float('inf') else  dis[dst]

            

        
