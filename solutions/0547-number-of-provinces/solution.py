
def dfs(graph,i,vis):
    vis[i]=True
    for node in range(len(graph[i])):
        if graph[i][node]==1 and vis[node]==False:
            dfs(graph,node,vis)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c=0
        n=len(isConnected)
        vis=[False]*(n)
        for i in range(n):
            if vis[i]==False:
                dfs(isConnected,i,vis)
                c+=1
        return c
        
