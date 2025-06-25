from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        vis=[-1]*(n)
        cancolor=True
        for i in range(n):
            if vis[i]==-1:
                vis[i]=0
                queue=deque([])
                queue.append((i,-1))
                while queue:
                    x=queue.popleft()
                    c=vis[x[0]]
                    for neigh in graph[x[0]]:
                        if vis[neigh]==-1:
                            vis[neigh]=c^1
                            queue.append((neigh,x[0]))
                        elif neigh!=x[1]:
                            if c==vis[neigh]:
                                cancolor=False
                                break
        return cancolor
    

                
        
