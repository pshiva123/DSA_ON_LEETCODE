class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][j]=0
        for u,v,w in edges:
            dist[u][v],dist[v][u]=w,w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]!=float('inf') and dist[k][j]!=float('inf'):
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        cnt=[]
        for i in range(n):
            cur=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    cur+=1
            cnt.append(cur)
        mini=cnt[0]
        mini_index=0
        for i in range(1,n):
            if cnt[i]<=mini:
                mini=cnt[i]
                mini_index=i
        return mini_index


        
