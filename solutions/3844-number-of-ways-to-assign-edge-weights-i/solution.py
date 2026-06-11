import heapq
from collections import deque
from functools import lru_cache
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n=len(edges)+1
        graph=[[] for i in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        mod=int(1e9+7)
        dis=[-1]*(n+1)
        dis[1]=0
        q=deque([1])
        while q:
            node=q.popleft()
            for neigh in graph[node]:
                if dis[neigh]==-1:
                    dis[neigh]=dis[node]+1
                    q.append(neigh)
    
        length=max(dis[1:])
        ways = pow(2, length-1, mod)
        return ways






        
