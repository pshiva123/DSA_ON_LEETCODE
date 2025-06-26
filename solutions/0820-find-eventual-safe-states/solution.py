from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans=[]
        n=len(graph)
        indegree=[0]*n
        rev_graph=[[] for _ in range(n)]
        for i in range(n):
            for x in graph[i]:
                rev_graph[x].append(i)
        for i in range(n):
            for node in rev_graph[i]:
                indegree[node]+=1
        queue=deque([i for i in range(n) if indegree[i]==0])
        while queue:
            node=queue.popleft()
            ans.append(node)
            for neigh in rev_graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh) 
        return sorted(ans)
    




        
