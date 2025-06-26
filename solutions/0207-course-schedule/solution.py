from collections import deque
class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        indegree=[0]*n
        for i in p:
            u,v=i[0],i[1]
            graph[v].append(u)
            indegree[u]+=1
        queue=deque([i for i in range(n) if indegree[i]==0])
        ans=[]
        while queue:
            node=queue.popleft()
            ans.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh) 
        return len(ans)==n       
        
        
