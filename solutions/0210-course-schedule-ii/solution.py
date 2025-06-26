
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for i in prerequisites:
            u,v=i[0],i[1]
            graph[v].append(u)
        ans=[]
        vis=[0]*(numCourses)
        detected=False
        print(graph)
        for i in range(numCourses):
            if vis[i]==0:
                detected=detected or dfs(graph,i,vis,ans)
        print(detected)
        if detected:
            return []
        return ans[::-1]
        


def dfs(graph,node,vis,ans):
    vis[node]=1
    for neigh in graph[node]:
        if vis[neigh]==1:
            return True
        if vis[neigh]==0:
            if dfs(graph,neigh,vis,ans):
                return True
    ans.append(node)
    vis[node]=2
    return False





        
