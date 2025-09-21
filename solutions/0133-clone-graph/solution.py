"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        vis=set()
        q=deque([node])
        vis.add(node)
        while q:
            node1=q.popleft()
            if not node1:
                break
            vis.add(node1)
            for neigh in node1.neighbors:
                if neigh not in vis:
                    q.append(neigh)
        n=len(vis)
        if n==1:
            return Node(1,None)
        
        adj=[[]for _ in range(n+1)]
        vis=set()
        q=deque([node])
        vis.add(node)
        while q:
            node1=q.popleft()
            if not node1:
                break
            vis.add(node1)
            for neigh in node1.neighbors:
                if neigh.val not in adj[node1.val]:
                    adj[node1.val].append(neigh.val)
                if neigh not in vis:
                    q.append(neigh)
        nodes=[Node(i,[]) for i in range(0,n+1)]
        #print(adj)
        #print(nodes)
        for i in range(1,n+1):
            for neighvals in adj[i]:
                nodes[i].neighbors.append(nodes[neighvals])
        return nodes[1]
        
            
            


                
