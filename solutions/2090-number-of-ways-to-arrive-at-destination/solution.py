import heapq
from collections import deque
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        m=int(1e9+7)
        graph=[[] for _ in range(n)]
        heap=[]
        for u,v,time in roads:
            graph[u].append([v,time])
            graph[v].append([u,time])
        heapq.heappush(heap,(0,0))
        dis=[float('inf')]*n
        dis[0]=0
        ways=[0]*n
        ways[0]=1
        while heap:
            cost,node=heapq.heappop(heap)
            for neigh,time in graph[node]:
                if dis[neigh]==cost+time:
                    ways[neigh]=(ways[neigh]+ways[node])%m
                elif dis[neigh]>cost+time:
                    ways[neigh]=(ways[node])%m
                    dis[neigh]=cost+time
                    heapq.heappush(heap,(dis[neigh],neigh))
        #print(ways)
        return ways[-1]
            

        
