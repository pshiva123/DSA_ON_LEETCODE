
def dfs(node,graph,vis):
    for i in range(len(graph)):
        if graph[node][i]==1 and vis[i]==False:
            vis[i]=True
            dfs(i,graph,vis)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt=0
        n=len(isConnected)
        vis=[False]*(n)
        for i in range(n):
            if vis[i] is False:
                cnt+=1
                vis[i]=True
                dfs(i,isConnected,vis)
        return cnt
            

        
        
