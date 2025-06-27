from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        queue=deque([])
        graph=[[] for _ in range(n+1)]
        for t in times:
            u,v,w=t[0],t[1],t[2]
            graph[u].append([v,w])
        queue.append((k,0))
        dis=[float('inf')]*(n+1)
        dis[0]=0
        dis[k]=0
        while queue:
            node,curdis=queue.popleft()
            for neigh,weight in graph[node]:
                if dis[neigh]>curdis+weight:
                    dis[neigh]=curdis+weight
                    queue.append((neigh,dis[neigh]))
        for i in dis:
            if i==float('inf'):
                return -1
        return max(dis)

        
